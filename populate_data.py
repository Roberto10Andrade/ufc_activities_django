#!/usr/bin/env python3
"""
Script para popular o banco de dados com atividades de exemplo
"""
import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ufc_activities_django.settings')
django.setup()

from activities.models import Activity, ActivityTag, ActivityRequirement

def create_sample_data():
    """Criar dados de exemplo"""
    
    # Criar tags
    tags_data = [
        'programação', 'web', 'python', 'django', 'javascript', 'react',
        'inteligência artificial', 'machine learning', 'pesquisa', 'extensão',
        'workshop', 'curso', 'seminário', 'tecnologia', 'inovação'
    ]
    
    tags = {}
    for tag_name in tags_data:
        tag, created = ActivityTag.objects.get_or_create(name=tag_name)
        tags[tag_name] = tag
        if created:
            print(f"Tag criada: {tag_name}")
    
    # Criar atividades de exemplo
    activities_data = [
        {
            'title': 'Curso de Desenvolvimento Web com Django',
            'description': 'Aprenda a desenvolver aplicações web modernas usando Django, um dos frameworks Python mais populares. O curso aborda desde conceitos básicos até técnicas avançadas de desenvolvimento.',
            'type': 'COURSE',
            'status': 'UPCOMING',
            'start_date': date.today() + timedelta(days=30),
            'end_date': date.today() + timedelta(days=90),
            'time': '19:00 - 22:00',
            'location': 'Laboratório de Informática 1',
            'coordinator': 'Prof. Carlos Silva',
            'participants': 25,
            'tags': ['programação', 'web', 'python', 'django'],
            'requirements': [
                'Conhecimentos básicos de Python',
                'Notebook próprio',
                'Disponibilidade para atividades práticas'
            ]
        },
        {
            'title': 'Workshop de Inteligência Artificial',
            'description': 'Workshop intensivo sobre IA e Machine Learning, explorando algoritmos, ferramentas e aplicações práticas na resolução de problemas reais.',
            'type': 'WORKSHOP',
            'status': 'ACTIVE',
            'start_date': date.today() - timedelta(days=5),
            'end_date': date.today() + timedelta(days=2),
            'time': '14:00 - 18:00',
            'location': 'Auditório Principal',
            'coordinator': 'Profa. Ana Santos',
            'participants': 40,
            'tags': ['inteligência artificial', 'machine learning', 'tecnologia'],
            'requirements': [
                'Conhecimentos básicos de programação',
                'Interesse em IA e ML'
            ]
        },
        {
            'title': 'Seminário de Inovação Tecnológica',
            'description': 'Evento que reúne pesquisadores, estudantes e profissionais para discutir as últimas tendências em tecnologia e inovação.',
            'type': 'SEMINAR',
            'status': 'UPCOMING',
            'start_date': date.today() + timedelta(days=15),
            'end_date': date.today() + timedelta(days=15),
            'time': '08:00 - 17:00',
            'location': 'Centro de Convenções',
            'coordinator': 'Prof. João Oliveira',
            'participants': 100,
            'tags': ['tecnologia', 'inovação', 'pesquisa'],
            'requirements': [
                'Inscrição prévia obrigatória'
            ]
        },
        {
            'title': 'Projeto de Extensão: Inclusão Digital',
            'description': 'Projeto voltado para levar conhecimentos de informática básica para comunidades carentes, promovendo inclusão digital.',
            'type': 'EXTENSION',
            'status': 'ACTIVE',
            'start_date': date.today() - timedelta(days=60),
            'end_date': date.today() + timedelta(days=120),
            'time': '08:00 - 12:00',
            'location': 'Comunidades locais',
            'coordinator': 'Profa. Maria Fernanda',
            'participants': 15,
            'tags': ['extensão', 'inclusão digital', 'comunidade'],
            'requirements': [
                'Disponibilidade para trabalho em campo',
                'Conhecimentos básicos de informática'
            ]
        },
        {
            'title': 'Pesquisa em Computação Quântica',
            'description': 'Grupo de pesquisa dedicado ao estudo de algoritmos quânticos e suas aplicações em problemas computacionais complexos.',
            'type': 'RESEARCH',
            'status': 'ACTIVE',
            'start_date': date.today() - timedelta(days=180),
            'end_date': date.today() + timedelta(days=365),
            'time': '14:00 - 18:00',
            'location': 'Laboratório de Pesquisa Avançada',
            'coordinator': 'Prof. Roberto Andrade',
            'participants': 8,
            'tags': ['pesquisa', 'computação quântica', 'algoritmos'],
            'requirements': [
                'Graduação em Ciência da Computação ou áreas afins',
                'Conhecimentos avançados em matemática',
                'Dedicação de pelo menos 20h semanais'
            ]
        }
    ]
    
    for activity_data in activities_data:
        # Extrair tags e requisitos
        activity_tags = activity_data.pop('tags', [])
        requirements = activity_data.pop('requirements', [])
        
        # Criar atividade
        activity, created = Activity.objects.get_or_create(
            title=activity_data['title'],
            defaults=activity_data
        )
        
        if created:
            print(f"Atividade criada: {activity.title}")
            
            # Adicionar tags
            for tag_name in activity_tags:
                if tag_name in tags:
                    activity.tags.add(tags[tag_name])
            
            # Adicionar requisitos
            for req_text in requirements:
                ActivityRequirement.objects.create(
                    activity=activity,
                    requirement=req_text
                )
        else:
            print(f"Atividade já existe: {activity.title}")

if __name__ == '__main__':
    print("Populando banco de dados com dados de exemplo...")
    create_sample_data()
    print("Dados criados com sucesso!")
    print(f"Total de atividades: {Activity.objects.count()}")
    print(f"Total de tags: {ActivityTag.objects.count()}")

