from django.urls import path
from .views import Record, Login, Logout, Profile

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/', Profile.as_view(), name="profile"),
]
