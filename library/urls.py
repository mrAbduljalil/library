from django.urls import path
from .views import books_list,book_detail

urlpatterns = [
    path('', books_list),
    path('book/<int:book_id>/', book_detail),
]
