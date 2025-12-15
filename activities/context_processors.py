from datetime import datetime


def accessibility_settings(request):
    """
    Context processor que disponibiliza as preferências de acessibilidade
    para todos os templates.
    """
    return {
        'font_size': request.session.get('font_size', 'normal'),
        'contrast': request.session.get('contrast', 'normal'),
        'dyslexia': request.session.get('dyslexia', False),
    }


def current_year(request):
    """
    Context processor para disponibilizar o ano atual no footer.
    """
    return {
        'now': datetime.now(),
    }
