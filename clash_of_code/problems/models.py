import django.conf
from django.contrib.auth import get_user_model
import django.core.validators
import django.db.models
from django.utils.translation import gettext_lazy as _
import tinymce.models

User = get_user_model()


class LanguageChoices(django.db.models.TextChoices):
    Python_3_11 = 'Py3.11', 'Python 3.11'


class VerdictChoice(django.db.models.TextChoices):
    Accept = 'AC', _('Accept')
    Compilation_error = 'CE', _('Compilation error')
    Wrong_answer = 'WA', _('Wrong answer')
    Time_limit = 'TL', _('Time limit')
    Runtime_error = 'RE', _('Runtime error')
    Memory_limit = 'ML', _('Memory limit')
    In_queue = 'IQ', _('In queue')
    In_processing = 'IP', _('In processing')


class Tag(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name=_('name'),
        max_length=75,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class ProblemManager(django.db.models.Manager):
    def is_public(self):
        return self.filter(
            is_public=True,
        )

    def add_authors(self):
        return self.is_public().select_related('author')

    def all_problem_list(self):
        return self.add_authors().only(
            'title',
            'author',
            'difficult',
            'tags__name',
        )


class Problem(django.db.models.Model):
    objects = ProblemManager()

    title = django.db.models.CharField(
        verbose_name=_('title'),
        max_length=75,
    )

    author = django.db.models.ForeignKey(
        to=User,
        verbose_name=_('author'),
        on_delete=django.db.models.CASCADE,
        related_name='tasks',
    )

    description = tinymce.models.HTMLField(
        verbose_name=_('description'),
        help_text=_('Explain the idea of the task'),
        max_length=100000,
    )

    input_format = tinymce.models.HTMLField(
        verbose_name=_('input data format'),
        help_text=_('Input data format'),
        max_length=50000,
        null=True,
        blank=True,
    )

    output_format = tinymce.models.HTMLField(
        verbose_name=_('output data format'),
        help_text=_('Output data format'),
        max_length=50000,
        null=True,
        blank=True,
    )

    is_public = django.db.models.BooleanField(
        verbose_name=_('is public'),
        help_text=_(
            'If you open the task for public access, other users will be able to add'
            ' it to their contests, and moderation will be able to evaluate it and add'
            ' it to the general pool of tasks',
        ),
        default=False,
    )

    difficult = django.db.models.PositiveIntegerField(
        verbose_name=_('difficult'),
        help_text=_('Assess the complexity of your task'),
        validators=[
            django.core.validators.MaxValueValidator(100),
        ],
    )

    author_solution = django.db.models.TextField(
        verbose_name=_('author solution'),
        help_text=_(
            "The author's solution is to take a long time to pass all the tests",
        ),
        max_length=8000,
        null=True,
        blank=True,
    )

    author_language = django.db.models.TextField(
        verbose_name=_('author language'),
        choices=LanguageChoices,
        null=True,
        blank=True,
    )

    tags = django.db.models.ManyToManyField(
        to=Tag,
        verbose_name=_('tags'),
        related_name='tasks',
        blank=True,
    )

    time_limit = django.db.models.IntegerField(
        default=1,
        validators=(
            django.core.validators.MaxValueValidator(5),
            django.core.validators.MinValueValidator(1),
        ),
    )
    memory_limit = django.db.models.IntegerField(
        default=256,
        validators=(
            django.core.validators.MaxValueValidator(512),
            django.core.validators.MinValueValidator(64),
        ),
    )

    is_correct = django.db.models.BooleanField(
        verbose_name=_('is correct'),
        help_text=_("Shows whether the author's solution is correct"),
        default=False,
    )

    status = django.db.models.CharField(
        verbose_name=_('status checked'),
        choices=VerdictChoice,
        default=VerdictChoice.In_queue,
    )

    test_error = django.db.models.IntegerField(
        verbose_name=_('test error'),
        blank=True,
        null=True,
    )

    logs = django.db.models.TextField(
        verbose_name=_('logs'),
        blank=True,
        null=True,
    )

    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title[:20]

    class Meta:
        verbose_name = _('problem')
        verbose_name_plural = _('problems')


class TestCase(django.db.models.Model):
    problem = django.db.models.ForeignKey(
        Problem,
        verbose_name=_('problem'),
        on_delete=django.db.models.CASCADE,
        related_name='tests',
    )

    is_sample = django.db.models.BooleanField(
        verbose_name=_('is sample'),
        help_text=_('If True, then this test will be shown as an example.'),
        default=False,
    )

    input_data = django.db.models.TextField(
        verbose_name=_('input data'),
        help_text=_(
            'Input data for the test. It will be passed '
            'to the program during execution via the standard stream',
        ),
    )

    output_data = django.db.models.TextField(
        verbose_name=_('output data'),
        help_text=_(
            'Test output. The program should output exactly this text in this format',
        ),
    )

    number = django.db.models.PositiveIntegerField(
        verbose_name=_('number of test'),
        default=1,
    )

    def __str__(self):
        return self.problem.title[:20] + ' ' + str(self.number)

    class Meta:
        verbose_name = _('test case')
        verbose_name_plural = _('tests cases')
        unique_together = ['problem', 'number']
        ordering = ['number']
