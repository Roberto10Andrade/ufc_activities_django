# 🎯 UFC Activities - Gerenciador de Atividades e Tarefas

Sistema web desenvolvido em Django para gerenciamento de atividades acadêmicas e tarefas da UFC Sobral, com foco em acessibilidade e usabilidade.

## 🚀 Funcionalidades

### 📊 Dashboard Interativo
- **Estatísticas em Tempo Real**: Total de atividades, pendentes, em progresso e concluídas
- **Visualizações Intuitivas**: Cards coloridos com informações importantes
- **Ações Rápidas**: Acesso direto às funcionalidades principais

### 📅 Gerenciamento de Atividades
- **CRUD Completo**: Criar, visualizar, editar e excluir atividades
- **Categorização**: Tipos de atividades (Curso, Workshop, Seminário, Pesquisa, Extensão)
- **Status**: Controle de status (Ativo, Próximo, Concluído, Cancelado)
- **Filtros Avançados**: Busca por tipo, status, coordenador, local
- **Paginação**: Performance otimizada para grandes volumes

### 🎯 Gerenciamento de Tarefas
- **Sistema Completo**: Criação e acompanhamento de tarefas
- **Prioridades**: Baixa, Média, Alta, Urgente
- **Status**: Pendente, Em Progresso, Concluída, Cancelada, Em Espera
- **Categorias**: Trabalho, Estudo, Pessoal, Saúde, Financeiro, Família
- **Progresso Visual**: Barras de progresso de 0-100%
- **Responsáveis**: Atribuição de usuários
- **Datas**: Controle de início, vencimento e conclusão

### ♿ Acessibilidade
- **Contraste Alto**: Modo de alto contraste para melhor legibilidade
- **Modo Invertido**: Cores invertidas para usuários com necessidades especiais
- **Tamanhos de Fonte**: Normal, Grande, Maior
- **Fonte para Dislexia**: OpenDyslexic para melhor leitura
- **Atalhos de Teclado**: Navegação rápida (Alt+A, Alt+T, Alt+C)
- **Transições Suaves**: Animações acessíveis

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Tailwind CSS
- **Ícones**: Font Awesome
- **Banco de Dados**: SQLite (desenvolvimento)
- **Python**: 3.13+

## 📦 Instalação

### Pré-requisitos
- Python 3.8+
- pip
- Git

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/ufc-activities-django.git
   cd ufc-activities-django
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências Python**
   ```bash
   pip install -r requirements.txt
   ```

4. **Compile o Tailwind CSS**
   ```bash
   cd theme/static_src
   npm install
   npm run build
   cd ../..
   ```

5. **Configure o banco de dados**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário**
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema**
   - URL: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 🎨 Interface e Design

### 🎯 Dashboard
- **Layout Responsivo**: Adaptável a todos os dispositivos
- **Cards Informativos**: Estatísticas visuais com gradientes
- **Navegação Intuitiva**: Menu lateral com ícones
- **Tema Claro/Escuro**: Alternância automática

### 📱 Responsividade
- **Mobile First**: Design otimizado para dispositivos móveis
- **Breakpoints**: Adaptação para tablet e desktop
- **Touch Friendly**: Botões e elementos otimizados para toque

### 🎨 Paleta de Cores
- **Primária**: Azul (#3b82f6)
- **Secundária**: Laranja (#f59e0b)
- **Sucesso**: Verde (#10b981)
- **Aviso**: Amarelo (#f59e0b)
- **Erro**: Vermelho (#ef4444)

## 🔧 Configuração

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Configurações de Produção
Para produção, configure:
- `DEBUG=False`
- Banco de dados PostgreSQL/MySQL
- Servidor web (Nginx + Gunicorn)
- HTTPS

## 📚 Estrutura do Projeto

```
ufc_activities_django/
├── accounts/                 # App de autenticação
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── activities/               # App principal
│   ├── models.py            # Modelos de dados
│   ├── views.py             # Views e lógica
│   ├── forms.py             # Formulários
│   └── urls.py              # URLs
├── templates/               # Templates HTML
│   ├── base.html            # Template base
│   ├── dashboard/           # Templates do dashboard
│   ├── activities/           # Templates de atividades
│   └── tasks/               # Templates de tarefas
├── static/                  # Arquivos estáticos
│   ├── css/                 # Estilos CSS
│   ├── js/                  # JavaScript
│   └── images/              # Imagens
├── media/                   # Uploads de usuários
└── requirements.txt         # Dependências
```

## 🚀 Funcionalidades Avançadas

### 🔍 Sistema de Busca
- **Busca Inteligente**: Por título, descrição, coordenador
- **Filtros Múltiplos**: Status, tipo, data
- **Resultados Paginados**: Performance otimizada

### 📊 Relatórios
- **Estatísticas**: Gráficos e métricas
- **Exportação**: Dados em diferentes formatos
- **Filtros Temporais**: Por período

### 👥 Gestão de Usuários
- **Autenticação**: Login/logout seguro
- **Permissões**: Controle de acesso
- **Perfis**: Informações do usuário

## 🧪 Testes

```bash
# Executar testes
python manage.py test

# Testes com cobertura
coverage run --source='.' manage.py test
coverage report
```

## 📈 Performance

### Otimizações Implementadas
- **Paginação**: Carregamento otimizado
- **Cache**: Dados em cache
- **Lazy Loading**: Carregamento sob demanda
- **Compressão**: Assets comprimidos

<<<<<<< HEAD
### Métricas
- **Tempo de Resposta**: < 200ms
- **Lighthouse Score**: 90+
- **Acessibilidade**: WCAG 2.1 AA

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Roberto Andrade**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Roberto Andrade](https://linkedin.com/in/roberto-andrade)

## 🙏 Agradecimentos

- UFC Sobral pelo apoio
- Comunidade Django
- Contribuidores do projeto

## 📞 Suporte

Para suporte, entre em contato:
- Email: suporte@ufc-activities.com
- Issues: [GitHub Issues](https://github.com/seu-usuario/ufc-activities-django/issues)

---

⭐ **Se este projeto foi útil, considere dar uma estrela!**
=======
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


