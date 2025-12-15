from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import JsonResponse

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
        
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(coordinator__icontains=search) |
                Q(location__icontains=search)
            )
        
        activity_type = self.request.GET.get('type')
        if activity_type:
            queryset = queryset.filter(type=activity_type)
            
        status = self.request.GET.get('status')
        if status:
            if status == 'UPCOMING':
                queryset = queryset.filter(status__in=['PENDING', 'UPCOMING'])
            elif status == 'ACTIVE':
                queryset = queryset.filter(status__in=['IN_PROGRESS', 'ACTIVE'])
            else:
                queryset = queryset.filter(status=status)
        
        start_date = self.request.GET.get('start_date')
        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        
        end_date = self.request.GET.get('end_date')
        if end_date:
            queryset = queryset.filter(start_date__lte=end_date)
            
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


class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_form.html'
    success_url = reverse_lazy('activity_list')

    def form_valid(self, form):
        messages.success(self.request, 'Atividade criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar atividade. Verifique os dados.')
        return super().form_invalid(form)


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activities/activity_form.html'
    success_url = reverse_lazy('activity_list')

    def form_valid(self, form):
        messages.success(self.request, 'Atividade atualizada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar atividade. Verifique os dados.')
        return super().form_invalid(form)


class ActivityDeleteView(DeleteView):
    model = Activity
    template_name = 'activities/delete.html'
    success_url = reverse_lazy('activity_list')
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Atividade excluída com sucesso!')
        return super().post(request, *args, **kwargs)


def dashboard_view(request):
    """View para o dashboard com estatísticas"""
    context = {
        'total_activities': Activity.objects.count(),
        'active_activities': Activity.objects.filter(status__in=['IN_PROGRESS', 'ACTIVE']).count(),
        'upcoming_activities': Activity.objects.filter(status__in=['PENDING', 'UPCOMING']).count(),
        'completed_activities': Activity.objects.filter(status='COMPLETED').count(),
        'recent_activities': Activity.objects.order_by('-created_at')[:5],
        'activities_by_type': Activity.objects.values('type').annotate(count=Count('type')),
    }
    return render(request, 'dashboard/index.html', context)


def search_view(request):
    """View para a página de busca"""
    queryset = Activity.objects.all()
    
    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(coordinator__icontains=search) |
            Q(location__icontains=search)
        )
    
    activity_type = request.GET.get('type')
    if activity_type:
        queryset = queryset.filter(type=activity_type)
        
    status = request.GET.get('status')
    if status:
        if status == 'UPCOMING':
            queryset = queryset.filter(status__in=['PENDING', 'UPCOMING'])
        elif status == 'ACTIVE':
            queryset = queryset.filter(status__in=['IN_PROGRESS', 'ACTIVE'])
        else:
            queryset = queryset.filter(status=status)
        
    queryset = queryset.order_by('-created_at')
    
    context = {
        'activities': queryset,
        'activity_types': Activity.ACTIVITY_TYPES,
        'status_choices': Activity.STATUS_CHOICES,
    }
    return render(request, 'activities/search.html', context)



