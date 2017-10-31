from django.conf.urls import url
from .views import LocatorSerialView, LocatorFetch, AllScu, mapview, timeview,indexview,polyview
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^devicelocation/scu_id=(?P<scu_id>\w+)&lat=(?P<lat>\d+(\.\d+)?)&lon=(?P<lon>\d+(\.\d+)?)$',
        LocatorSerialView),
    url(r'^getlocation/(?P<scu_id>\w+)/$', LocatorFetch),
    url(r'^map/(?P<id>\w+)/$',mapview),
    url(r'^allscu/$', AllScu),
    url(r'^getlocation/(?P<scu_id>\w+)/(?P<start>.*)/(?P<end>.*)/$', timeview),
    url(r'^map/(?P<scu_id>\w+)/(?P<start>.*)/(?P<end>.*)/', polyview),
    # url(r'^$', TemplateView.as_view(template_name= 'index.html'))
    url(r'^$', indexview)

]

