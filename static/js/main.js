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

    // Função para atualizar posição do botão toggle
    function updateToggleButtonPosition(isVisible) {
        const toggleBtn = document.getElementById('sidebar-toggle');
        const toggleIcon = document.getElementById('sidebar-toggle-icon');
        if (!toggleBtn) return;
        
        // Usar classes CSS ao invés de style inline para garantir que funcione
        requestAnimationFrame(() => {
            if (isVisible) {
                // Sidebar visível: adicionar classe para mover botão
                toggleBtn.classList.remove('toggle-sidebar-closed');
                toggleBtn.classList.add('toggle-sidebar-open');
                // Mudar ícone para X quando aberto
                if (toggleIcon) {
                    toggleIcon.classList.remove('fa-bars');
                    toggleIcon.classList.add('fa-times');
                    toggleBtn.setAttribute('aria-label', 'Ocultar menu');
                }
            } else {
                // Sidebar oculta: adicionar classe para voltar botão
                toggleBtn.classList.remove('toggle-sidebar-open');
                toggleBtn.classList.add('toggle-sidebar-closed');
                // Mudar ícone para menu quando fechado
                if (toggleIcon) {
                    toggleIcon.classList.remove('fa-times');
                    toggleIcon.classList.add('fa-bars');
                    toggleBtn.setAttribute('aria-label', 'Mostrar menu');
                }
            }
        });
    }

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
            updateToggleButtonPosition(true);
        } else {
            sidebar.classList.add('hidden');
            sidebar.classList.add('md:hidden');
            sidebar.classList.add('sidebar-hidden');
            contentWrapper.classList.add('without-sidebar');
            contentWrapper.classList.remove('with-sidebar');
            const footer = document.getElementById('app-footer');
            if (footer) { footer.classList.add('without-sidebar'); footer.classList.remove('with-sidebar'); }
            updateToggleButtonPosition(false);
        }

        toggleBtn.addEventListener('click', () => {
            const visibleNow = !sidebar.classList.contains('sidebar-hidden');
            if (visibleNow) {
                // Fechar sidebar
                sidebar.classList.add('sidebar-hidden');
                sidebar.classList.add('hidden');
                sidebar.classList.add('md:hidden');
                contentWrapper.classList.add('without-sidebar');
                contentWrapper.classList.remove('with-sidebar');
                const footer = document.getElementById('app-footer');
                if (footer) { footer.classList.add('without-sidebar'); footer.classList.remove('with-sidebar'); }
                localStorage.setItem('sidebarVisible', 'false');
                // Atualizar posição do botão com pequeno delay para sincronizar com animação
                setTimeout(() => updateToggleButtonPosition(false), 10);
            } else {
                // Abrir sidebar
                sidebar.classList.remove('hidden');
                sidebar.classList.remove('md:hidden');
                sidebar.classList.remove('sidebar-hidden');
                contentWrapper.classList.add('with-sidebar');
                contentWrapper.classList.remove('without-sidebar');
                const footer = document.getElementById('app-footer');
                if (footer) { footer.classList.add('with-sidebar'); footer.classList.remove('without-sidebar'); }
                localStorage.setItem('sidebarVisible', 'true');
                // Atualizar posição do botão com pequeno delay para sincronizar com animação
                setTimeout(() => updateToggleButtonPosition(true), 10);
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

    // Indicador móvel da navegação (inspirado no exemplo React)
    function updateNavIndicator() {
        const indicator = document.getElementById('nav-indicator');
        const navLinks = document.querySelectorAll('.nav-menu-link');
        const currentPath = window.location.pathname;
        
        if (!indicator || navLinks.length === 0) return;
        
        // Remover classe active de todos os links
        navLinks.forEach(link => {
            link.classList.remove('active');
        });
        
        // Encontrar o link ativo
        let activeLink = null;
        let bestMatch = null;
        let bestMatchLength = 0;
        
        navLinks.forEach(link => {
            try {
                const linkUrl = new URL(link.href, window.location.origin);
                const linkPath = linkUrl.pathname;
                
                // Match exato tem prioridade máxima
                if (currentPath === linkPath) {
                    activeLink = link;
                    bestMatch = link;
                    bestMatchLength = linkPath.length;
                } 
                // Se não houver match exato, procurar o mais específico (mais longo)
                else if (linkPath !== '/' && currentPath.startsWith(linkPath)) {
                    if (linkPath.length > bestMatchLength) {
                        bestMatch = link;
                        bestMatchLength = linkPath.length;
                    }
                }
            } catch (e) {
                // Ignorar erros de URL inválida
                console.debug('Erro ao processar URL do link:', e);
            }
        });
        
        // Usar o melhor match encontrado
        if (!activeLink && bestMatch) {
            activeLink = bestMatch;
        }
        
        if (activeLink) {
            // Adicionar classe active ao link para estilização
            activeLink.classList.add('active');
            
            // Calcular posição do indicador de forma precisa
            const linkRect = activeLink.getBoundingClientRect();
            const navList = activeLink.closest('ul');
            if (!navList) return;
            
            const navListRect = navList.getBoundingClientRect();
            
            // Calcular posição relativa dentro do ul (sem considerar scroll, pois é absolute)
            const top = linkRect.top - navListRect.top;
            const height = linkRect.height;
            
            // Usar requestAnimationFrame para transição mais suave (similar ao React)
            requestAnimationFrame(() => {
                indicator.style.top = `${top}px`;
                indicator.style.height = `${height}px`;
                
                // Mostrar indicador com fade-in suave
                if (indicator.classList.contains('opacity-0')) {
                    indicator.classList.remove('opacity-0');
                    // Pequeno delay para forçar reflow e garantir transição suave
                    requestAnimationFrame(() => {
                        indicator.style.opacity = '1';
                    });
                } else {
                    indicator.style.opacity = '1';
                }
            });
        } else {
            // Esconder indicador se não houver link ativo
            requestAnimationFrame(() => {
                indicator.style.opacity = '0';
                setTimeout(() => {
                    indicator.classList.add('opacity-0');
                }, 200); // Aguardar a transição de opacity
            });
        }
    }
    
    // Função debounced para atualizar indicador (evita múltiplas chamadas)
    let updateTimeout = null;
    function updateNavIndicatorDelayed() {
        if (updateTimeout) {
            clearTimeout(updateTimeout);
        }
        updateTimeout = setTimeout(() => {
            updateNavIndicator();
            updateTimeout = null;
        }, 50);
    }
    
    // Atualizar indicador imediatamente ao carregar
    updateNavIndicator();
    
    // Atualizar ao redimensionar a janela
    let resizeTimeout = null;
    window.addEventListener('resize', () => {
        if (resizeTimeout) {
            clearTimeout(resizeTimeout);
        }
        resizeTimeout = setTimeout(() => {
            updateNavIndicator();
            // Atualizar posição do botão toggle também
            const sidebar = document.getElementById('sidebar');
            if (sidebar) {
                const isVisible = !sidebar.classList.contains('sidebar-hidden') && 
                                 !sidebar.classList.contains('hidden');
                updateToggleButtonPosition(isVisible);
            }
        }, 100);
    });
    
    // Atualizar quando a sidebar aparecer/desaparecer
    const sidebarForIndicator = document.getElementById('sidebar');
    if (sidebarForIndicator) {
        const sidebarObserver = new MutationObserver(() => {
            // Verificar estado da sidebar para atualizar indicador
            const isVisible = !sidebarForIndicator.classList.contains('hidden') && 
                             !sidebarForIndicator.classList.contains('sidebar-hidden');
            
            // Atualizar indicador se sidebar estiver visível
            if (isVisible) {
                updateNavIndicatorDelayed();
            }
            
            // Atualizar posição do botão toggle
            updateToggleButtonPosition(isVisible);
        });
        
        sidebarObserver.observe(sidebarForIndicator, {
            attributes: true,
            attributeFilter: ['class'],
            childList: false,
            subtree: false
        });
    }
    
    // Atualizar quando navegar usando botões do browser (back/forward)
    window.addEventListener('popstate', updateNavIndicatorDelayed);
    
    // Atualizar quando clicar em qualquer link do menu
    document.querySelectorAll('.nav-menu-link').forEach(link => {
        link.addEventListener('click', () => {
            // Usar um delay maior para garantir que a navegação ocorreu
            setTimeout(updateNavIndicator, 150);
        });
    });
    
    // Atualizar após o carregamento completo da página
    if (document.readyState === 'complete') {
        updateNavIndicator();
    } else {
        window.addEventListener('load', () => {
            setTimeout(updateNavIndicator, 100);
        });
    }
    
    // Observar mudanças no DOM que possam afetar a posição dos links
    const navContainer = document.querySelector('nav.flex-1');
    if (navContainer) {
        const domObserver = new MutationObserver(() => {
            updateNavIndicatorDelayed();
        });
        
        domObserver.observe(navContainer, {
            childList: true,
            subtree: true,
            attributes: false
        });
    }
});

