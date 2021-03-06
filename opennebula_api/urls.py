from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TemplateCreateView, TemplateDetailsView,\
                   VmCreateView, VmDetailsView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^templates/$', TemplateCreateView.as_view(), name="template_create"),
    url(r'^templates/(?P<pk>[0-9]+)/$', TemplateDetailsView.as_view(),
        name="templates_details"),
    
    url(r'^vms/$', VmCreateView.as_view(), name="vm_create"),
    url(r'^vms/(?P<pk>[0-9]+)/$', VmDetailsView.as_view(),
        name="vm_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
