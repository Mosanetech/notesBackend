from django.urls import path
from users.views import RegisterView,LoginView,Helloworldview,ProfileView

urlpatterns =[
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('hello/',Helloworldview.as_view(),name="HelloWorld"),
    path('profile/',ProfileView.as_view(),name="user-profile")

]