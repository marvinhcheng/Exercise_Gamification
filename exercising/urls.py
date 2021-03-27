from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView

from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'exercising'
urlpatterns = [
    path('', TemplateView.as_view(template_name="exercising/index.html")),
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='exercising/index.html'), name='logout'),
    path('goals/', views.GoalsListView.as_view(), name='goals'),
    # path('logs/', views.LogsListView.as_view(), name='logs'),
    path('logs/', views.add_exercise, name='logs')
]