from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home_page'),

    path('courses/', views.courses, name='courses_all'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:course_id>/', views.course_update, name='course_update'),
    path('courses/<int:course_id>/', views.courses_show, name='courses_show'),
    path('courses/delete/<int:course_id>/', views.course_delete, name="delete_course"),
    path('courses/search/', views.search_title, name="search_title"),

    path('api/courses/', views.json_courses, name='json_data'),
    path('api/courses/<int:course_id>/', views.api_courses_show, name='api_courses_show'),
]
