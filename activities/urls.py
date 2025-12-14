from django.urls import path
from . import views

urlpatterns = [
    # Página inicial é o dashboard
    path('', views.dashboard_view, name='dashboard'),
    # Página de busca
    path('search/', views.search_view, name='search'),
    # Lista de atividades
    path('atividades/', views.ActivityListView.as_view(), name='activity_list'),
    path('atividades/', views.ActivityListView.as_view(), name='atividades'),
    path('atividades/<int:pk>/', views.ActivityDetailView.as_view(), name='activity_detail'),
    path('atividades/new/', views.ActivityCreateView.as_view(), name='activity_create'),
    path('atividades/edit/<int:pk>/', views.ActivityUpdateView.as_view(), name='activity_update'),
    path('atividades/delete/<int:pk>/', views.ActivityDeleteView.as_view(), name='activity_delete'),
]

