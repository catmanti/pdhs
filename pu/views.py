from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Institution, DSDivision, MOHDivision
from data.models import Population
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin


class MOHDivisionListView(ListView):
    """Show a list of MOH Divisions"""

    model = MOHDivision
    paginate_by = 14


class DSDivisionListView(ListView):
    """Show a list of DS Divisions"""

    model = DSDivision
    paginate_by = 14


class InstitutionListView(ListView):
    """Show List of all institutions"""

    model = Institution
    paginate_by = 14
    # context_object_name = "items"

    # For Dougnut chart
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get group by count of institution types like BHA, MOH, PMCU use below
        # context["type"] = Institution.objects.values("type").annotate(Count("type"))

        # Get the count group by DS Divisions
        context["type"] = Institution.objects.values("ds_division__name").annotate(
            Count("ds_division__name")
        )
        return context


class InstitutionCreateView(PermissionRequiredMixin, CreateView):
    """Create a new Institution"""

    permission_required = "pu.add_institution"
    login_url = "/login"
    model = Institution
    fields = ["name", "type", "ds_division"]

    def get_success_url(self):
        return reverse("institutions")


class DSDivisionCreateView(PermissionRequiredMixin, CreateView):
    """Create a new DSDivision"""

    model = DSDivision
    fields = ["name", "moh_division"]

    permission_required = "pu.add_dsdivision"
    login_url = "/login"

    def get_success_url(self):
        return reverse("ds-view")
