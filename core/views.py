from django.shortcuts import render
#from .models import Document

def accueil(request):
    return render(request, 'core/accueil.html')

def sixieme(request):
    return render(request, 'core/college/sixieme.html')
"""def sixieme(request):
    docs = Document.objects.filter(page="sixieme")
    return render(request, 'core/college/sixieme.html', {
        'docs': docs,
        'classe': '6',
        'niveau': 'Sixième'
    })"""

def septieme(request):
    return render(request, 'core/college/septieme.html')


"""def septieme(request):
    docs = Document.objects.filter(page="septieme")
    return render(request, 'core/college/septieme.html', {
        'docs': docs,
        'classe': '7',
        'niveau': 'Septième'
    })"""


def huitieme(request):
    return render(request, 'core/college/huitieme.html')

def neuvieme(request):
    return render(request, 'core/college/neuvieme.html')

def seconde(request):
    return render(request, 'core/lycee_general/seconde/seconde.html')

def premiere_gfm(request):
    return render(request, 'core/lycee_general/GFM/premiere_gfm.html')
def terminal_gfm(request):
    return render(request, 'core/lycee_general/GFM/terminal_gfm.html')

def premiere_ogrh(request):
    return render(request, 'core/lycee_general/OGRH/premiere_ogrh.html')
def terminal_ogrh(request):
    return render(request, 'core/lycee_general/OGRH/terminal_ogrh.html')

def premiere_iag(request):
    return render(request, 'core/lycee_general/IAG/premiere_iag.html')
def terminal_iag(request):
    return render(request, 'core/lycee_general/IAG/terminal_iag.html')

def tice(request):
    return render(request, 'core/tice.html')



from .models import Visite

def accueil(request):
    visite, created = Visite.objects.get_or_create(id=1)

    if not request.session.get('visite'):
        visite.total += 1
        visite.save()
        request.session['visite'] = True

    return render(request, 'core/accueil.html', {
        'visites': visite.total
    })