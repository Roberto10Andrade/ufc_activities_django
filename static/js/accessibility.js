// Controles de Acessibilidade

// Toggle do painel de acessibilidade
function toggleAccessibility() {
    const panel = document.getElementById('accessibility-controls');
    panel.classList.toggle('hidden');
}

// Configuração de tamanho da fonte
function setFontSize(size) {
    document.body.setAttribute('data-font-size', size);
    localStorage.setItem('fontSize', size);
    
    // Atualizar botões ativos
    document.querySelectorAll('#accessibility-controls button').forEach(btn => {
        btn.classList.remove('bg-primary-500', 'text-white');
        btn.classList.add('bg-gray-100', 'dark:bg-gray-700');
    });
    
    event.target.classList.remove('bg-gray-100', 'dark:bg-gray-700');
    event.target.classList.add('bg-primary-500', 'text-white');
}

// Configuração de contraste
function setContrast(contrast) {
    document.body.setAttribute('data-contrast', contrast);
    localStorage.setItem('contrast', contrast);
    
    // Atualizar botões ativos
    const contrastButtons = document.querySelectorAll('#accessibility-controls div:nth-child(2) button');
    contrastButtons.forEach(btn => {
        btn.classList.remove('bg-primary-500', 'text-white');
        btn.classList.add('bg-gray-100', 'dark:bg-gray-700');
    });
    
    event.target.classList.remove('bg-gray-100', 'dark:bg-gray-700');
    event.target.classList.add('bg-primary-500', 'text-white');
}

// Toggle da fonte para dislexia
function toggleDyslexiaFont() {
    const isDyslexia = event.target.checked;
    document.body.setAttribute('data-dyslexia', isDyslexia);
    localStorage.setItem('dyslexiaFont', isDyslexia);
}

// Carregar configurações salvas
function loadAccessibilitySettings() {
    const fontSize = localStorage.getItem('fontSize') || 'normal';
    const contrast = localStorage.getItem('contrast') || 'normal';
    const dyslexiaFont = localStorage.getItem('dyslexiaFont') === 'true';
    
    document.body.setAttribute('data-font-size', fontSize);
    document.body.setAttribute('data-contrast', contrast);
    document.body.setAttribute('data-dyslexia', dyslexiaFont);
    
    // Atualizar interface
    const dyslexiaCheckbox = document.querySelector('#accessibility-controls input[type="checkbox"]');
    if (dyslexiaCheckbox) {
        dyslexiaCheckbox.checked = dyslexiaFont;
    }
}

// Atalhos de teclado para acessibilidade
document.addEventListener('keydown', function(e) {
    // Alt + A para abrir painel de acessibilidade
    if (e.altKey && e.key === 'a') {
        e.preventDefault();
        toggleAccessibility();
    }
    
    // Alt + T para alternar tema
    if (e.altKey && e.key === 't') {
        e.preventDefault();
        toggleTheme();
    }
});

// Inicializar configurações ao carregar a página
document.addEventListener('DOMContentLoaded', loadAccessibilitySettings);

