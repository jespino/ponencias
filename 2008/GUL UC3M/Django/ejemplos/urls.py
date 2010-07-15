from django.conf.urls.defaults import *
from django.views.generic import list_detail, create_update, simple
from django.http import HttpResponse
from ejemplos.holamundo.views import holamundo, holapersona, holapersonaplantilla, holapersonacheetah, fallo
from ejemplos.miniblog.views import index, index2, new, delete
from ejemplos.miniblog.models import Post

urlpatterns = patterns('',
    # Example:
    # (r'^ejemplos/', include('ejemplos.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^holamundo/$', holamundo ),
    (r'^holadirect/(?P<nombre>\w+)/$', simple.direct_to_template, {'template':"holamundo/holadirect.html"}),
    (r'^holayo/$', holapersona, {'nombre':'Jesus'} ),
    (r'^holapersona/(?P<nombre>\w+)/$', holapersona ),
    (r'^holapersonaplantilla/(?P<nombre>\w+)/$', holapersonaplantilla ),
    (r'^holapersonacheetah/(?P<nombre>\w+)/$', holapersonacheetah ),
    (r'^fallo/', fallo),
    (r'^index/$', index ),
    (r'^index2/$', index2 ),
    (r'^new/$', new ),
    (r'^delete/(?P<id>\d+)/$', delete ),
    (r'^generic_index/', list_detail.object_list, {'queryset': Post.objects.all(), 'allow_empty':True, 'template_name':"posts/generic_index.html"}),
    (r'^generic_new/', create_update.create_object, {'model': Post, 'post_save_redirect':"/generic_index", 'template_name':"posts/generic_new.html"}),
)
