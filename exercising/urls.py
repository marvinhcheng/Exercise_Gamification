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

    path('music/', views.music, name='music'),
    path('map/', views.map, name='map'),


    path('groups/create_group/', views.CreateGroup.as_view(), name="create_group"),
    path('groups/', views.GroupListView.as_view(), name="groups"),
    path('groups/<int:group_id>', views.group_detail, name="group_detail"),
    path('groups/<int:group_id>/add/', views.add_to_group, name="add_to_group"),
    path('groups/<int:group_id>/join/', views.join_group),
    path('groups/<int:group_id>/edit/remove/', views.remove_from_group, name="remove_from_group"),
    path('groups/<int:group_id>/edit/', views.edit_group.as_view(), name="edit"),
    path('groups/<int:group_id>/edit/delete_group/', views.delete_group, name="delete_group"),

    path('diet/', TemplateView.as_view(template_name="exercising/diet.html")),
    path('diet/keto/', TemplateView.as_view(template_name="exercising/keto.html")),
    path('exercise_tips/', TemplateView.as_view(template_name="exercising/tips.html")),
<<<<<<< HEAD
    path('exercise_tips/bench/', TemplateView.as_view(template_name="exercising/bench.html")),
    path('diet/vegetarian/', TemplateView.as_view(template_name="exercising/vegetarian.html")),
    path('diet/paleo/', TemplateView.as_view(template_name="exercising/paleo.html")),
    path('diet/mediterranean/', TemplateView.as_view(template_name="exercising/mediterranean.html")),
    path('diet/atkins/', TemplateView.as_view(template_name="exercising/atkins.html")),
    path('exercise_tips/bicep/', TemplateView.as_view(template_name="exercising/bicep.html")),
    path('exercise_tips/shoulder/', TemplateView.as_view(template_name="exercising/shoulder.html")),
    path('exercise_tips/rows/', TemplateView.as_view(template_name="exercising/rows.html")),
    path('exercise_tips/crunches/', TemplateView.as_view(template_name="exercising/crunches.html")),
    path('exercise_tips/squat/', TemplateView.as_view(template_name="exercising/squat.html")),
    path('exercise_tips/legpress/', TemplateView.as_view(template_name="exercising/legpress.html")),
    path('exercise_tips/calf/', TemplateView.as_view(template_name="exercising/calf.html"))
    
=======
    path('exercise_tips/bench/', TemplateView.as_view(template_name="exercising/bench.html"))

>>>>>>> main
]