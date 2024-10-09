from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),  # ホーム画面
    path('question/<int:pk>/', views.question_view, name='question'),  # 問題ページ
    path('submit_answer/<int:pk>/', views.submit_answer, name='submit_answer'),  # 回答送信
    path('result/', views.result_view, name='result'),  # 結果画面
]
