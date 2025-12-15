class AccessibilityMiddleware:
    """
    Middleware para gerenciar preferências de acessibilidade via sessão.
    Processa parâmetros GET: font_size, contrast, dyslexia
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Processar parâmetros de acessibilidade da URL e salvar na sessão
        if 'font_size' in request.GET:
            font_size = request.GET.get('font_size')
            if font_size in ('normal', 'large', 'larger'):
                request.session['font_size'] = font_size
        
        if 'contrast' in request.GET:
            contrast = request.GET.get('contrast')
            if contrast in ('normal', 'high'):
                request.session['contrast'] = contrast
        
        if 'dyslexia' in request.GET:
            dyslexia = request.GET.get('dyslexia')
            request.session['dyslexia'] = dyslexia == 'true'
        
        response = self.get_response(request)
        return response
