from django.shortcuts import redirect, render
from django.views.generic import TemplateView

# Create your views here.
'''
class HomePageView(TemplateView):
    template_name = "home.html"
'''

def home(request):
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'home.html')