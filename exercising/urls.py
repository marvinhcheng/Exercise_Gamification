from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView


app_name = 'exercising'
urlpatterns = [
    path('', TemplateView.as_view(template_name="app/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='app/index.html'), name='logout'),
    path('goals/', views.GoalsListView.as_view(), name='goals'),
    path('logs/', views.LogsListView.as_view(), name='logs'),
]