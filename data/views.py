from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Population
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
from pu.models import Institution
from django.http import HttpResponse


# class Logout(LogoutView):
def home(request):
    meta = request.META
    for k, v in meta.items():
        print(k, " = ", v)
    return HttpResponse("Hi")


class Login(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("population-chart")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class PopulationChartView(TemplateView):
    """Show Population in ChartJS This is the home-page"""

    template_name = "data/population_chart.html"

    # For Dougnut chart
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["population"] = Population.objects.all()
        return context


class TestView(PermissionRequiredMixin, TemplateView):
    """View For testing"""

    permission_required = "pu.view_institution"
    login_url = "/login"
    # template_name = "data/test.html"
    template_name = "data/pichart.html"

    # template_name = "data/barchart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = Institution.objects.values("type").annotate(Count("type"))
        return context
