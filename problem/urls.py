from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^question/$',views.question,name='question'),
    url(r'^answer_/(?P<num>[0-9])/$',views.answer,name='answer'),
]