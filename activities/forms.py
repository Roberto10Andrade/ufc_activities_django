from django import forms
from .models import Activity, ActivityTag, ActivityRequirement


class ActivityForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=ActivityTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tags'
    )
    
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite cada requisito em uma linha separada'}),
        required=False,
        label='Requisitos',
        help_text='Digite cada requisito em uma linha separada'
    )
    
    class Meta:
        model = Activity
        fields = [
            'title', 'description', 'type', 'status', 
            'start_date', 'end_date', 'time', 'location', 
            'coordinator', 'participants', 'image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da atividade'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição detalhada da atividade'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 14:00 - 18:00'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local da atividade'}),
            'coordinator': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do coordenador'}),
            'participants': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Preencher tags existentes
            self.fields['tags'].initial = self.instance.tags.all()
            # Preencher requisitos existentes
            requirements = self.instance.requirements.all().values_list('requirement', flat=True)
            self.fields['requirements'].initial = '\n'.join(requirements)
    
    def save(self, commit=True):
        instance = super().save(commit=commit)
        
        if commit:
            # Salvar tags
            tags = self.cleaned_data.get('tags')
            if tags:
                instance.tags.set(tags)
            else:
                instance.tags.clear()
            
            # Salvar requisitos
            requirements_text = self.cleaned_data.get('requirements', '')
            if requirements_text:
                # Remover requisitos existentes
                instance.requirements.all().delete()
                # Adicionar novos requisitos
                requirements_list = [req.strip() for req in requirements_text.split('\n') if req.strip()]
                for req in requirements_list:
                    ActivityRequirement.objects.create(activity=instance, requirement=req)
            else:
                instance.requirements.all().delete()
        
        return instance


class ActivitySearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar atividades...',
            'autocomplete': 'off'
        })
    )
    type = forms.ChoiceField(
        choices=[('', 'Todos os tipos')] + Activity.ACTIVITY_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[('', 'Todos os status')] + Activity.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

