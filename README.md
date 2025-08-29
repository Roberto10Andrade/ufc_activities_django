# UFC Sobral Activities - Django MPA

Versão Multi-Page Application (MPA) do sistema de gerenciamento de atividades acadêmicas da UFC Sobral, desenvolvida com Django.

## 📋 Sobre o Projeto

Esta é uma versão MPA (Multi-Page Application) do projeto original UFC Sobral Activities, convertida de Next.js para Django. O sistema permite o gerenciamento completo de atividades acadêmicas como cursos, workshops, seminários, projetos de pesquisa e extensão.

## ✨ Funcionalidades

### 🔐 Autenticação
- Sistema de login e registro de usuários
- Controle de acesso baseado em permissões
- Interface responsiva para autenticação

### 📊 Dashboard
- Visão geral das atividades acadêmicas
- Estatísticas em tempo real
- Gráficos de atividades por tipo
- Lista de atividades recentes
- Ações rápidas para usuários autenticados

### 🎯 Gerenciamento de Atividades
- **Listagem**: Visualização de todas as atividades com filtros avançados
- **Detalhes**: Página individual para cada atividade com informações completas
- **Criação**: Formulário completo para criação de novas atividades
- **Edição**: Atualização de atividades existentes (para usuários autenticados)
- **Busca**: Sistema de busca por título, descrição e coordenador

### 🏷️ Sistema de Tags
- Tags automáticas baseadas no conteúdo
- Filtros por tags
- Organização visual das atividades

### 📱 Interface Responsiva
- Design adaptável para desktop, tablet e mobile
- Tema claro/escuro com alternância automática
- Acessibilidade aprimorada
- Componentes interativos com Tailwind CSS

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 5.2.5**: Framework web Python
- **SQLite**: Banco de dados (desenvolvimento)
- **Pillow**: Processamento de imagens

### Frontend
- **HTML5**: Estrutura semântica
- **Tailwind CSS**: Framework CSS utilitário
- **JavaScript**: Interatividade e funcionalidades dinâmicas
- **Font Awesome**: Ícones

### Recursos Adicionais
- **Django Admin**: Interface administrativa
- **CSRF Protection**: Proteção contra ataques CSRF
- **Responsive Design**: Layout adaptável
- **Dark Mode**: Suporte a tema escuro

## 📁 Estrutura do Projeto

```
ufc_activities_django/
├── ufc_activities_django/          # Configurações do projeto
│   ├── settings.py                 # Configurações Django
│   ├── urls.py                     # URLs principais
│   └── wsgi.py                     # Configuração WSGI
├── activities/                     # App principal
│   ├── models.py                   # Modelos de dados
│   ├── views.py                    # Views/Controllers
│   ├── forms.py                    # Formulários
│   ├── urls.py                     # URLs do app
│   └── admin.py                    # Configuração do admin
├── accounts/                       # App de autenticação
│   ├── views.py                    # Views de auth
│   └── urls.py                     # URLs de auth
├── templates/                      # Templates HTML
│   ├── base.html                   # Template base
│   ├── activities/                 # Templates de atividades
│   ├── dashboard/                  # Templates do dashboard
│   └── registration/               # Templates de auth
├── static/                         # Arquivos estáticos
│   ├── css/                        # Estilos CSS
│   └── js/                         # Scripts JavaScript
└── media/                          # Uploads de mídia
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd ufc_activities_django
```

2. **Instale as dependências**:
```bash
pip install django pillow
```

3. **Execute as migrações**:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Crie um superusuário** (opcional):
```bash
python manage.py createsuperuser
```

5. **Popule com dados de exemplo**:
```bash
python populate_data.py
```

6. **Execute o servidor de desenvolvimento**:
```bash
python manage.py runserver 0.0.0.0:8000
```

7. **Acesse o sistema**:
   - Sistema: http://localhost:8000
   - Admin: http://localhost:8000/admin

### Usuário de Teste
- **Usuário**: admin
- **Senha**: admin123

## 📊 Modelos de Dados

### Activity (Atividade)
- **title**: Título da atividade
- **description**: Descrição detalhada
- **type**: Tipo (Curso, Workshop, Seminário, Pesquisa, Extensão, Outro)
- **status**: Status (Ativo, Próximo, Concluído, Cancelado)
- **start_date/end_date**: Datas de início e fim
- **time**: Horário
- **location**: Local
- **coordinator**: Coordenador
- **participants**: Número de participantes
- **created_at/updated_at**: Timestamps

### ActivityTag (Tag de Atividade)
- **name**: Nome da tag
- **activities**: Relacionamento many-to-many com atividades

### ActivityRequirement (Requisito de Atividade)
- **activity**: Atividade relacionada
- **requirement**: Texto do requisito

## 🎨 Características da Interface

### Design System
- **Cores**: Paleta baseada em azul (primary) com suporte a tema escuro
- **Tipografia**: Fonte system com hierarquia clara
- **Espaçamento**: Grid system consistente
- **Componentes**: Cards, botões, formulários e badges padronizados

### Responsividade
- **Mobile First**: Design otimizado para dispositivos móveis
- **Breakpoints**: sm (640px), md (768px), lg (1024px), xl (1280px)
- **Layout**: Grid flexível que se adapta ao tamanho da tela

### Acessibilidade
- **Navegação por teclado**: Suporte completo
- **Screen readers**: Elementos semânticos e ARIA labels
- **Contraste**: Cores que atendem às diretrizes WCAG
- **Focus indicators**: Indicadores visuais claros

## 🔄 Diferenças do Projeto Original

### Arquitetura
- **SPA → MPA**: Mudança de Single-Page para Multi-Page Application
- **Next.js → Django**: Framework JavaScript para Python
- **Client-side → Server-side**: Renderização no servidor

### Funcionalidades Mantidas
- ✅ Listagem de atividades com filtros
- ✅ Detalhes de atividades
- ✅ Sistema de busca
- ✅ Interface responsiva
- ✅ Tema claro/escuro

### Funcionalidades Adicionadas
- ✅ Sistema de autenticação completo
- ✅ Dashboard com estatísticas
- ✅ Painel administrativo
- ✅ Criação/edição de atividades
- ✅ Sistema de tags
- ✅ Requisitos de atividades

## 🚀 Deploy e Produção

### Configurações de Produção
Para deploy em produção, considere:

1. **Configurar variáveis de ambiente**:
```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
SECRET_KEY = 'sua-chave-secreta-segura'
```

2. **Usar banco de dados robusto**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ufc_activities',
        # ... outras configurações
    }
}
```

3. **Configurar arquivos estáticos**:
```python
STATIC_ROOT = '/caminho/para/static'
MEDIA_ROOT = '/caminho/para/media'
```

4. **Usar servidor WSGI**:
```bash
gunicorn ufc_activities_django.wsgi:application
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Créditos

- **Projeto Original**: [UFC Sobral Activities](https://github.com/Roberto10Andrade/ufc-sobral-activities)
- **Conversão para Django**: Desenvolvido como versão MPA do sistema original
- **Universidade Federal do Ceará - Campus Sobral**

## 📞 Suporte

Para suporte e dúvidas:
- Abra uma issue no GitHub
- Entre em contato através dos canais oficiais da UFC Sobral

---

**UFC Sobral Activities - Django MPA** 🎓
*Sistema de Gerenciamento de Atividades Acadêmicas*

