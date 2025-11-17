from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('COURSE', 'Curso'),
        ('WORKSHOP', 'Workshop'),
        ('SEMINAR', 'Seminário'),
        ('RESEARCH', 'Pesquisa'),
        ('EXTENSION', 'Extensão'),
        ('OTHER', 'Outro'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Ativo'),
        ('UPCOMING', 'Próximo'),
        ('COMPLETED', 'Concluído'),
        ('CANCELLED', 'Cancelado'),
    ]
    
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    type = models.CharField('Tipo', max_length=20, choices=ACTIVITY_TYPES, default='OTHER')
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='UPCOMING')
    start_date = models.DateField('Data de Início')
    end_date = models.DateField('Data de Fim')
    time = models.CharField('Horário', max_length=50, blank=True)
    location = models.CharField('Local', max_length=200)
    coordinator = models.CharField('Coordenador', max_length=100)
    participants = models.IntegerField('Participantes', default=0)
    image = models.ImageField('Imagem', upload_to='activities/', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
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
