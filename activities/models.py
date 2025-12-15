from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):
    class ActivityType(models.TextChoices):
        COURSE = 'COURSE', _('Curso')
        WORKSHOP = 'WORKSHOP', _('Workshop')
        SEMINAR = 'SEMINAR', _('Seminário')
        RESEARCH = 'RESEARCH', _('Pesquisa')
        EXTENSION = 'EXTENSION', _('Extensão')
        OTHER = 'OTHER', _('Outro')

    class ActivityStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pendente')
        UPCOMING = 'UPCOMING', _('Pendente')
        IN_PROGRESS = 'IN_PROGRESS', _('Em Andamento')
        ACTIVE = 'ACTIVE', _('Em Andamento')
        COMPLETED = 'COMPLETED', _('Concluída')
        CANCELLED = 'CANCELLED', _('Cancelada')

    ACTIVITY_TYPES = [
        ('COURSE', 'Curso'),
        ('WORKSHOP', 'Workshop'),
        ('SEMINAR', 'Seminário'),
        ('RESEARCH', 'Pesquisa'),
        ('EXTENSION', 'Extensão'),
        ('OTHER', 'Outro'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('UPCOMING', 'Pendente'),
        ('IN_PROGRESS', 'Em Andamento'),
        ('ACTIVE', 'Em Andamento'),
        ('COMPLETED', 'Concluída'),
        ('CANCELLED', 'Cancelada'),
    ]
    
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Título'),
        help_text=_('Título da atividade (mínimo 3 caracteres)')
    )
    description = models.TextField(
        validators=[MinLengthValidator(10)],
        verbose_name=_('Descrição'),
        help_text=_('Descrição detalhada da atividade (mínimo 10 caracteres)')
    )
    type = models.CharField(
        max_length=20,
        choices=ActivityType.choices,
        default=ActivityType.COURSE,
        verbose_name=_('Tipo')
    )
    status = models.CharField(
        max_length=20,
        choices=ActivityStatus.choices,
        default=ActivityStatus.PENDING,
        verbose_name=_('Status')
    )
    start_date = models.DateField(verbose_name=_('Data de Início'))
    end_date = models.DateField(verbose_name=_('Data de Término'))
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('Horário')
    )
    location = models.CharField(
        max_length=200,
        verbose_name=_('Local'),
        help_text=_('Ex: Laboratório de Informática 1')
    )
    coordinator = models.CharField(
        max_length=200,
        verbose_name=_('Coordenador'),
        help_text=_('Ex: Prof. João Silva')
    )
    participants = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_('Número de Participantes'),
        help_text=_('Mínimo 1 participante'),
        default=1
    )
    image = models.ImageField('Imagem', upload_to='activities/', blank=True, null=True)
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('URL da Imagem')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Criado em')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Atualizado em')
    )
    
    class Meta:
        verbose_name = _('Atividade')
        verbose_name_plural = _('Atividades')
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError({
                'end_date': 'A data de término deve ser posterior à data de início.'
            })

    def get_absolute_url(self):
        return reverse('activity_detail', kwargs={'pk': self.pk})
    
    def get_gradient_class(self):
        """Retorna a classe de gradiente baseada no tipo da atividade"""
        gradients = {
            'COURSE': 'from-blue-500 to-indigo-600',
            'WORKSHOP': 'from-purple-500 to-violet-600',
            'SEMINAR': 'from-emerald-500 to-teal-600',
            'RESEARCH': 'from-amber-500 to-orange-600',
            'EXTENSION': 'from-rose-500 to-pink-600',
            'OTHER': 'from-gray-500 to-slate-600'
        }
        return gradients.get(self.type, 'from-gray-500 to-slate-600')
    
    def get_icon(self):
        """Retorna o ícone emoji baseado no tipo da atividade"""
        icons = {
            'COURSE': '📚',
            'WORKSHOP': '🛠️',
            'SEMINAR': '🎯',
            'RESEARCH': '🔬',
            'EXTENSION': '🤝',
            'OTHER': '📌'
        }
        return icons.get(self.type, '📌')


class ActivityTag(models.Model):
    name = models.CharField('Nome', max_length=50, unique=True)
    activities = models.ManyToManyField(Activity, related_name='tags', blank=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class ActivityRequirement(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='requirements')
    requirement = models.CharField('Requisito', max_length=200)
    
    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
    
    def __str__(self):
        return f"{self.activity.title} - {self.requirement}"
