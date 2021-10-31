from django.urls import path
from .views import Logout, Register, StockDetail, StockList, Login, Logout
urlpatterns = [
    path('register', Register.as_view()),
    path('stocks/',StockList.as_view()),
    path('stocks/<int:pk>/', StockDetail.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),
]