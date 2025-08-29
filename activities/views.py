from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import Activity, ActivityTag
from .forms import ActivityForm, ActivitySearchForm


class ActivityListView(ListView):
    model = Activity
    template_name = 'activities/list.html'
    context_object_name = 'activities'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Activity.objects.all()
        
        # Busca
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(coordinator__icontains=search) |
                Q(location__icontains=search)
            )
        
        # Filtros
        activity_type = self.request.GET.get('type')
        if activity_type:
            queryset = queryset.filter(type=activity_type)
            
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ActivitySearchForm(self.request.GET)
        context['activity_types'] = Activity.ACTIVITY_TYPES
        context['status_choices'] = Activity.STATUS_CHOICES
        return context


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activities/detail.html'
    context_object_name = 'activity'


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/create.html'
    success_url = reverse_lazy('activity_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Atividade criada com sucesso!')
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/edit.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Atividade atualizada com sucesso!')
        return super().form_valid(form)


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = 'activities/delete.html'
    success_url = reverse_lazy('activity_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Atividade excluída com sucesso!')
        return super().delete(request, *args, **kwargs)


def dashboard_view(request):
    """View para o dashboard com estatísticas"""
    context = {
        'total_activities': Activity.objects.count(),
        'active_activities': Activity.objects.filter(status='ACTIVE').count(),
        'upcoming_activities': Activity.objects.filter(status='UPCOMING').count(),
        'completed_activities': Activity.objects.filter(status='COMPLETED').count(),
        'recent_activities': Activity.objects.order_by('-created_at')[:5],
        'activities_by_type': Activity.objects.values('type').annotate(count=Count('type')),
    }
    return render(request, 'dashboard/index.html', context)
