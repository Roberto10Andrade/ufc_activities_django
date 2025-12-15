from django import forms
from .models import Activity, ActivityTag

FORM_INPUT_CLASS = 'w-full px-4 py-3 bg-white border-2 border-gray-200 rounded-lg text-base transition-all duration-200 focus:border-blue-500 focus:outline-none hover:border-blue-300 placeholder-gray-400'

class ActivityForm(forms.ModelForm):
    tags = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': FORM_INPUT_CLASS,
            'rows': 2,
            'placeholder': 'Digite as tags separadas por vírgula'
        }),
        label='Tags',
        help_text='Digite as tags separadas por vírgula (mínimo 1 tag obrigatória)'
    )

    class Meta:
        model = Activity
        fields = [
            'title', 'type', 'description', 'status',
            'start_date', 'end_date', 'location',
            'coordinator', 'participants'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': FORM_INPUT_CLASS,
                'placeholder': 'Digite o título da atividade'
            }),
            'description': forms.Textarea(attrs={
                'class': FORM_INPUT_CLASS,
                'rows': 4,
                'placeholder': 'Descreva os detalhes da atividade'
            }),
            'start_date': forms.DateInput(attrs={
                'class': FORM_INPUT_CLASS,
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': FORM_INPUT_CLASS,
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': FORM_INPUT_CLASS,
                'placeholder': 'Ex: Laboratório de Informática 1'
            }),
            'coordinator': forms.TextInput(attrs={
                'class': FORM_INPUT_CLASS,
                'placeholder': 'Ex: Prof. João Silva'
            }),
            'participants': forms.NumberInput(attrs={
                'class': FORM_INPUT_CLASS,
                'min': 1
            }),
            'status': forms.Select(attrs={
                'class': FORM_INPUT_CLASS
            }),
            'type': forms.Select(attrs={
                'class': FORM_INPUT_CLASS
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            tags_str = ', '.join([tag.name for tag in self.instance.tags.all()])
            self.fields['tags'].initial = tags_str

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title.strip()) < 3:
            raise forms.ValidationError('Título deve ter pelo menos 3 caracteres')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description.strip()) < 10:
            raise forms.ValidationError('Descrição deve ter pelo menos 10 caracteres')
        return description

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        if len(tag_list) == 0:
            raise forms.ValidationError('Adicione pelo menos uma tag')
        return tags

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError({
                'end_date': 'A data de término deve ser posterior à data de início.'
            })
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            tags_str = self.cleaned_data.get('tags', '')
            if tags_str:
                tag_names = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                tags = []
                for tag_name in tag_names:
                    tag, created = ActivityTag.objects.get_or_create(name=tag_name)
                    tags.append(tag)
                instance.tags.set(tags)
            else:
                instance.tags.clear()
        return instance


class ActivitySearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': FORM_INPUT_CLASS,
            'placeholder': 'Buscar atividades...',
            'autocomplete': 'off'
        })
    )
    type = forms.ChoiceField(
        choices=[('', 'Todos os tipos')] + Activity.ACTIVITY_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': FORM_INPUT_CLASS})
    )
    status = forms.ChoiceField(
        choices=[('', 'Todos os status')] + Activity.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': FORM_INPUT_CLASS})
    )
