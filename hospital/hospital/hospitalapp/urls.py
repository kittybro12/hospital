from django.urls import path
from hospitalapp import views 

urlpatterns = [
    path('',views.home,name= 'home'),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('main/',views.main,name='main'),
    path('about/',views.about,name='about'),   
     
]
