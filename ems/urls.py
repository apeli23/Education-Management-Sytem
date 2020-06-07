"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
# from main.sitemaps import SchoolSitemap, PrincipleSitemap
from main.views import (
    SchoolsListView, PrincipleView, CategoryView,
    StatusView, SubcountyView, SchoolView,
    CapacityView,
    # UploadsView,
    SubcountyListView,
    PrinciplesListView, CategoriesListView,
    StatusListView, SchoolDetailView, CapacityListView,
    CapacityUpdate, CapacityDeleteView, SchoolDeleteView,
    SchoolUpdateView, SubcountyDeleteView,
    SubcountyUpdateView,
    StatusUpdateView,
    CategoryUpdateVIew,
    PrincipleUpdateView,
    StatusDeleteView,
    CategoryDeleteView,
    PrincipleDeleteView,
    PrincipleDetailView,
    SignUp,
    Login,
    TotalSchoolsPerSubCounty
)
from django.conf.urls.static import static
from django.conf import settings

# sitemaps = {
#     'schools': SchoolSitemap,
#     'principles': PrincipleSitemap
# }

urlpatterns = [
    # admin url
    url(r'^admin/', admin.site.urls),
    # input urls
    url(r'^principle/new/$', PrincipleView.as_view(), name="principleForm"),
    url(r'^status/new/$', StatusView.as_view(), name="StatusForm"),
    url(r'^category/new/$', CategoryView.as_view(), name="CategoryForm"),
    url(r'^subcounty/new/$', SubcountyView.as_view(), name="SubcountyForm"),
    url(r'^school/new/$', SchoolView.as_view(), name="SchoolForm"),
    url(r'^capacity/new/$', CapacityView.as_view(), name="CapacityForm"),
    # list urls
    url(r'^$', SchoolsListView.as_view(), name="schools"),
    url(r'^subcounties/list/$', SubcountyListView.as_view(),
        name="subcounties"),
    url(r'^status/list/$', StatusListView.as_view(), name="statuses"),
    url(r'^category/list/$', CategoriesListView.as_view(), name="categories"),
    url(r'^principle/list/$', PrinciplesListView.as_view(), name="principles"),
    # file uploads bulk inputs
    # url(r'^upload/files/$', UploadsView.as_view(), name="uploads"),
    # detail links
    url(r'^school/detail/(?P<pk>[0-9]+)$',
        SchoolDetailView.as_view(), name="school_details"),
    url(r'^capacity/list/(?P<pk>[0-9]+)$',
        CapacityListView.as_view(), name="capacitylist"),
    url(r'^principle/detail/(?P<pk>[0-9]+)$',
        PrincipleDetailView.as_view(), name="principledetails"),
    # update links
    url(r'^capacity/update/(?P<pk>[0-9]+)$',
        CapacityUpdate.as_view(), name="capacityupdate"),
    url(r'^school/edit/(?P<pk>[0-9]+)$',
        SchoolUpdateView.as_view(), name="schoolupdate"),
    url(r'^principle/edit/(?P<pk>[0-9]+)$',
        PrincipleUpdateView.as_view(), name="principleupdate"),
    url(r'^category/edit/(?P<pk>[0-9]+)$',
        CategoryUpdateVIew.as_view(), name="categoryupdate"),
    url(r'^status/edit/(?P<pk>[0-9]+)$',
        StatusUpdateView.as_view(), name="statusupdate"),
    url(r'^subcounty/edit/(?P<pk>[0-9]+)$',
        SubcountyUpdateView.as_view(), name="subcountyupdate"),
    # delete links
    url(r'^capacity/delete/(?P<pk>[0-9]+)$',
        CapacityDeleteView.as_view(), name="capacitydelete"),
    url(r'^school/delete/(?P<pk>[0-9]+)$',
        SchoolDeleteView.as_view(), name="schooldelete"),
    url(r'^subcounty/delete/(?P<pk>[0-9]+)$',
        SubcountyDeleteView.as_view(), name="subcountydelete"),
    url(r'^principle/delete/(?P<pk>[0-9]+)$',
        PrincipleDeleteView.as_view(), name="principledelete"),
    url(r'^category/delete/(?P<pk>[0-9]+)$',
        CategoryDeleteView.as_view(), name="categorydelete"),
    url(r'^status/delete/(?P<pk>[0-9]+)$',
        StatusDeleteView.as_view(), name="statusdelete"),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'),
    url(r'^signup/$', SignUp.as_view(), name="signup"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^subcounty/stat/$', TotalSchoolsPerSubCounty.as_view(),
        name="substat")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
