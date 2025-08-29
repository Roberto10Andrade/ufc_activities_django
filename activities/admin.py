from django.contrib import admin
from .models import Activity, ActivityTag, ActivityRequirement


class ActivityRequirementInline(admin.TabularInline):
    model = ActivityRequirement
    extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'status', 'start_date', 'end_date', 'coordinator', 'participants']
    list_filter = ['type', 'status', 'start_date', 'created_at']
    search_fields = ['title', 'description', 'coordinator', 'location']
    date_hierarchy = 'start_date'
    ordering = ['-created_at']
    inlines = [ActivityRequirementInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'type', 'status')
        }),
        ('Datas e Horários', {
            'fields': ('start_date', 'end_date', 'time')
        }),
        ('Local e Coordenação', {
            'fields': ('location', 'coordinator', 'participants')
        }),
        ('Mídia', {
            'fields': ('image',)
        }),
    )


@admin.register(ActivityTag)
class ActivityTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['activities']


@admin.register(ActivityRequirement)
class ActivityRequirementAdmin(admin.ModelAdmin):
    list_display = ['activity', 'requirement']
    list_filter = ['activity']
    search_fields = ['requirement', 'activity__title']
