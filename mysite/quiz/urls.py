# urls.py
from django.urls import path 
from .views import QuizList, QuizUpdateDelete, JawabanList, JawabanUpdateDelete, CalculateQuizValue
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('quiz/', QuizList.as_view(), name= "create-quiz-list"),
    path('quiz/<int:pk>/', QuizUpdateDelete.as_view(), name= "quiz-details"),
    path('jawaban/', JawabanList.as_view(), name= "create-jawaban-list"),
    path('jawaban/<int:pk>/', JawabanUpdateDelete.as_view(), name= "jawaban-details"),
    path('calculate-quiz-value/', CalculateQuizValue.as_view(), name='calculate-quiz-value'),
]