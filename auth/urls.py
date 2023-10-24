from django.urls import path

from auth import views


urlpatterns = [
    path('creation/', views.RegisterUser,name="creation"),
    path('update/<int:id>/', views.UpdateUser,name="update"),
    path('login/', views.LoginUser,name="login"),
    path('delete/<int:id>/', views.DeleteUser,name="delete"),
]