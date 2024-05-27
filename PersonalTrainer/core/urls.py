from django.urls import path

from django.contrib.auth.views import LogoutView

from . import views

from core.views import CustomLoginView 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('aout', views.about, name='about'),
]
