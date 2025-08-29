// JavaScript Principal

// Toggle do menu do usuário
function toggleUserMenu() {
    const menu = document.getElementById('user-menu');
    menu.classList.toggle('hidden');
}

// Fechar menu ao clicar fora
document.addEventListener('click', function(e) {
    const userMenu = document.getElementById('user-menu');
    const userButton = document.querySelector('[onclick="toggleUserMenu()"]');
    
    if (userMenu && !userMenu.contains(e.target) && !userButton.contains(e.target)) {
        userMenu.classList.add('hidden');
    }
    
    const accessibilityPanel = document.getElementById('accessibility-controls');
    const accessibilityButton = document.querySelector('[onclick="toggleAccessibility()"]');
    
    if (accessibilityPanel && !accessibilityPanel.contains(e.target) && !accessibilityButton.contains(e.target)) {
        accessibilityPanel.classList.add('hidden');
    }
});

// Animação de fade-in para elementos
function animateElements() {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// Confirmação de exclusão
function confirmDelete(message) {
    return confirm(message || 'Tem certeza que deseja excluir este item?');
}

// Função para mostrar loading
function showLoading(element) {
    const spinner = document.createElement('div');
    spinner.className = 'spinner inline-block ml-2';
    element.appendChild(spinner);
    element.disabled = true;
}

// Função para esconder loading
function hideLoading(element) {
    const spinner = element.querySelector('.spinner');
    if (spinner) {
        spinner.remove();
    }
    element.disabled = false;
}

// Busca em tempo real (debounced)
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Aplicar busca com delay
const searchInput = document.querySelector('input[name="search"]');
if (searchInput) {
    const debouncedSearch = debounce(function() {
        const form = searchInput.closest('form');
        if (form) {
            form.submit();
        }
    }, 500);
    
    searchInput.addEventListener('input', debouncedSearch);
}

// Smooth scroll para âncoras
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Inicializar animações ao carregar
document.addEventListener('DOMContentLoaded', function() {
    animateElements();
    
    // Auto-hide messages após 5 segundos
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(alert => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        });
    }, 5000);

    // Sidebar toggle com persistência
    const sidebar = document.getElementById('sidebar');
    const contentWrapper = document.getElementById('contentWrapper');
    const toggleBtn = document.getElementById('sidebar-toggle');
    if (sidebar && contentWrapper && toggleBtn) {
        const saved = localStorage.getItem('sidebarVisible');
        const isVisible = saved === null ? false : saved === 'true';
        // Estado inicial
        if (isVisible) {
            sidebar.classList.remove('hidden');
            sidebar.classList.remove('md:hidden');
            sidebar.classList.remove('sidebar-hidden');
            contentWrapper.classList.add('with-sidebar');
            contentWrapper.classList.remove('without-sidebar');
            const footer = document.getElementById('app-footer');
            if (footer) { footer.classList.add('with-sidebar'); footer.classList.remove('without-sidebar'); }
        } else {
            sidebar.classList.add('hidden');
            sidebar.classList.add('md:hidden');
            sidebar.classList.add('sidebar-hidden');
            contentWrapper.classList.add('without-sidebar');
            contentWrapper.classList.remove('with-sidebar');
            const footer = document.getElementById('app-footer');
            if (footer) { footer.classList.add('without-sidebar'); footer.classList.remove('with-sidebar'); }
        }

        toggleBtn.addEventListener('click', () => {
            const visibleNow = !sidebar.classList.contains('sidebar-hidden');
            if (visibleNow) {
                sidebar.classList.add('sidebar-hidden');
                sidebar.classList.add('hidden');
                sidebar.classList.add('md:hidden');
                contentWrapper.classList.add('without-sidebar');
                contentWrapper.classList.remove('with-sidebar');
                const footer = document.getElementById('app-footer');
                if (footer) { footer.classList.add('without-sidebar'); footer.classList.remove('with-sidebar'); }
                localStorage.setItem('sidebarVisible', 'false');
            } else {
                sidebar.classList.remove('hidden');
                sidebar.classList.remove('md:hidden');
                sidebar.classList.remove('sidebar-hidden');
                contentWrapper.classList.add('with-sidebar');
                contentWrapper.classList.remove('without-sidebar');
                const footer = document.getElementById('app-footer');
                if (footer) { footer.classList.add('with-sidebar'); footer.classList.remove('without-sidebar'); }
                localStorage.setItem('sidebarVisible', 'true');
            }
        });
    }

    // Header animado somente na página inicial
    const header = document.getElementById('landing-header');
    if (header && window.location.pathname === '/') {
        // loaded
        setTimeout(() => header.classList.remove('opacity-0'), 0);
        // scroll behavior
        const onScroll = () => {
            if (window.scrollY > 20) {
                header.classList.remove('py-6');
                header.classList.add('py-4');
            } else {
                header.classList.add('py-6');
                header.classList.remove('py-4');
            }
        };
        onScroll();
        window.addEventListener('scroll', onScroll);
    }
});

