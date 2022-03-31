from django.urls import path

from .views import RegistrationView, LoginView, ActivationView, LogoutView, ForgotPasswordComplete, ForgotPassword, GetUser

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('activation/', ActivationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot-complete/', ForgotPasswordComplete.as_view()),
    path('forgot/', ForgotPassword.as_view()),
    path('user/', GetUser.as_view()),
]
