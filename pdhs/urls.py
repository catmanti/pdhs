"""pdhs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from data.views import (
    PopulationChartView,
    TemplateView,
    TestView,
    Login,
    LogoutView,
    home,
)
from pu.views import (
    InstitutionListView,
    InstitutionCreateView,
    DSDivisionListView,
    MOHDivisionListView,
    DSDivisionCreateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", Login.as_view(), name="logout"),
    path("home/", home, name="home"),
    path("logout/", LogoutView.as_view(), name="login"),
    path("", PopulationChartView.as_view(), name="population-chart"),
    path("test/", TestView.as_view(), name="test"),
    path("data/", InstitutionListView.as_view(), name="institutions"),
    path("data/ds/", DSDivisionListView.as_view(), name="ds-view"),
    path("data/moh/", MOHDivisionListView.as_view(), name="moh-view"),
    path("data/add/", InstitutionCreateView.as_view(), name="add-institution"),
    path("data/ds/add/", DSDivisionCreateView.as_view(), name="add-ds-division"),
    path("__debug__/", include("debug_toolbar.urls")),
]
