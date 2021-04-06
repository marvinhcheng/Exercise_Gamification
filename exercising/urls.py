from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView

from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'exercising'
urlpatterns = [
    path('', TemplateView.as_view(template_name="exercising/index.html")),
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='exercising/index.html'), name='logout'),
    path('goals/', views.add_goal, name='goals'),
    path('logs/', views.add_exercise, name='logs'),
    # path('groups/', views.create_group, name="create_group")
    path('groups/', TemplateView.as_view(template_name="exercising/group.html"), name="groups"),
    path('groups/create_group/', views.CreateGroup.as_view(), name="create_group"),
    path('groups/list/', views.GroupListView.as_view(), name="groupslist"),
    path('groups/list/<int:pk>', views.group_detail.as_view(), name="group_detail")
    # path('groups/detail/<int:pk>', views.group_detail, name='group_detail')
    # path('groups/<int:owner_id>', views.group_detail, name = 'detail')
]