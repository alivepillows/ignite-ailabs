# urls.py
from django.urls import path 
from .views import QuizList, QuizUpdateDelete
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('quiz/', QuizList.as_view(), name= "create-quiz-list"),
    path('quiz/<int:pk>/', QuizUpdateDelete.as_view(), name= "quiz-details")
]