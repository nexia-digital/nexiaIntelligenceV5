from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class nexiaIntelligenceHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'