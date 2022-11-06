
from django.urls import path, include
from account import views


urlpatterns = [
    path('registration/', views.UserRegistration.as_view()),
    path('<slug:user_name>', views.UserDetail.as_view()),

]

