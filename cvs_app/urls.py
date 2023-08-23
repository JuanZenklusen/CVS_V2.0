from django.urls import path
from .views import index, RegisterView, profile, create_academic_data, update_academic_data, delete_academic_data, add_job, about_me


urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='profile'),
    path('profile/academic', create_academic_data, name='academic'),
    path('profile/academic-update/<int:id>/', update_academic_data, name='update_academic_data'),
    path('profile/academic-delete/<int:id>/', delete_academic_data, name='delete_academic_data'),
    path('profile/add_job', add_job, name='add_job'),
    path('profile/about_me', about_me, name='about_me'),
]