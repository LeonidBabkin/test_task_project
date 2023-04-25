from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('', views.UserRegisterView.as_view(), name='register'),
]
