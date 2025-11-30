// Controles de Acessibilidade

// Estado global de acessibilidade
let accessibilityState = {
    fontSize: 'normal',
    contrast: 'normal',
    dyslexia: false
};

let isAccessibilityOpen = false;

// Carregar configurações salvas
document.addEventListener('DOMContentLoaded', function() {
    const savedSettings = localStorage.getItem('accessibility-settings');
    if (savedSettings) {
        accessibilityState = JSON.parse(savedSettings);
        applySettings(accessibilityState.fontSize, accessibilityState.contrast, accessibilityState.dyslexia);
    }
    updateButtonStates();
});

// Toggle do dropdown de acessibilidade
function toggleAccessibilityDropdown() {
    const content = document.getElementById('accessibility-content');
    const arrow = document.getElementById('accessibility-arrow');
    const button = document.getElementById('accessibilityBtn');
    
    isAccessibilityOpen = !isAccessibilityOpen;
    
    if (content) {
        if (isAccessibilityOpen) {
            content.style.maxHeight = content.scrollHeight + 'px';
            content.style.opacity = '1';
        } else {
            content.style.maxHeight = '0';
            content.style.opacity = '0';
        }
    }
    
    if (arrow) {
        if (isAccessibilityOpen) {
            arrow.style.transform = 'rotate(180deg)';
        } else {
            arrow.style.transform = 'rotate(0deg)';
        }
    }
    
    if (button) {
        button.setAttribute('aria-expanded', isAccessibilityOpen.toString());
    }
}

// Aplicar configurações
function applySettings(fontSize, contrast, dyslexia) {
    // Aplicar tamanho de fonte
    document.documentElement.setAttribute('data-font-size', fontSize);
    
    // Aplicar contraste
    document.documentElement.classList.remove('high-contrast', 'inverted-colors');
    if (contrast === 'high') {
        document.documentElement.classList.add('high-contrast');
    } else if (contrast === 'inverted') {
        document.documentElement.classList.add('inverted-colors');
    }
    
    // Aplicar fonte para dislexia
    if (dyslexia) {
        document.documentElement.classList.add('dyslexic-font');
    } else {
        document.documentElement.classList.remove('dyslexic-font');
    }
    
    // Atualizar estado e salvar
    accessibilityState = { fontSize, contrast, dyslexia };
    localStorage.setItem('accessibility-settings', JSON.stringify(accessibilityState));
    
    // Atualizar UI dos botões
    updateButtonStates();
}

// Atualizar estado visual dos botões
function updateButtonStates() {
    // Atualizar botões de fonte
    document.querySelectorAll('[data-font-btn]').forEach(btn => {
        const isActive = btn.getAttribute('data-font-btn') === accessibilityState.fontSize;
        btn.setAttribute('aria-pressed', isActive.toString());
        if (isActive) {
            btn.classList.remove('bg-white/10', 'text-white');
            btn.classList.add('bg-white', 'text-blue-600', 'shadow-md');
        } else {
            btn.classList.remove('bg-white', 'text-blue-600', 'shadow-md');
            btn.classList.add('bg-white/10', 'text-white');
        }
    });
    
    // Atualizar botões de contraste
    document.querySelectorAll('[data-contrast-btn]').forEach(btn => {
        const isActive = btn.getAttribute('data-contrast-btn') === accessibilityState.contrast;
        btn.setAttribute('aria-pressed', isActive.toString());
        if (isActive) {
            btn.classList.remove('bg-white/10', 'text-white');
            btn.classList.add('bg-white', 'text-blue-600', 'shadow-md');
        } else {
            btn.classList.remove('bg-white', 'text-blue-600', 'shadow-md');
            btn.classList.add('bg-white/10', 'text-white');
        }
    });
    
    // Atualizar botão de dislexia
    const dyslexiaBtn = document.getElementById('dyslexia-btn');
    const dyslexiaText = document.getElementById('dyslexia-text');
    if (dyslexiaBtn) {
        dyslexiaBtn.setAttribute('aria-pressed', accessibilityState.dyslexia.toString());
        if (accessibilityState.dyslexia) {
            dyslexiaBtn.classList.remove('bg-white/10', 'text-white');
            dyslexiaBtn.classList.add('bg-white', 'text-blue-600', 'shadow-md');
            if (dyslexiaText) dyslexiaText.textContent = 'Fonte Dislexia Ativa';
        } else {
            dyslexiaBtn.classList.remove('bg-white', 'text-blue-600', 'shadow-md');
            dyslexiaBtn.classList.add('bg-white/10', 'text-white');
            if (dyslexiaText) dyslexiaText.textContent = 'Fonte para Dislexia';
        }
    }
}

// Configuração de tamanho da fonte
function setFontSize(size) {
    applySettings(size, accessibilityState.contrast, accessibilityState.dyslexia);
}

// Configuração de contraste
function setContrast(contrast) {
    applySettings(accessibilityState.fontSize, contrast, accessibilityState.dyslexia);
}

// Toggle da fonte para dislexia
function toggleDyslexia() {
    applySettings(accessibilityState.fontSize, accessibilityState.contrast, !accessibilityState.dyslexia);
}

// Toggle do painel de acessibilidade (antigo - mantido para compatibilidade)
function toggleAccessibility() {
    const panel = document.getElementById('accessibility-controls');
    if (panel) {
        panel.classList.toggle('hidden');
    }
}

// Atalhos de teclado para acessibilidade
document.addEventListener('keydown', function(e) {
    // Alt + A para abrir painel de acessibilidade
    if (e.altKey && e.key === 'a') {
        e.preventDefault();
        toggleAccessibilityDropdown();
    }
    
    // Alt + T para alternar tema
    if (e.altKey && e.key === 't') {
        e.preventDefault();
        if (typeof toggleTheme === 'function') {
            toggleTheme();
        }
    }
});
