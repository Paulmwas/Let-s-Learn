from django.urls import path
from .views import signup, login_page, logout_page, profile_page

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
]