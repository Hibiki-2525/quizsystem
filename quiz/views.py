from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, UserAnswer 
from django.views import View  
  
class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'quiz/home.html')
top_page = SampleView.as_view()

# ホーム画面: 問題のリストを表示
def home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html', {'questions': questions})

# 問題の回答ページ
def question_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'quiz/question.html', {'question': question})

# 回答送信
def submit_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        user_answer = request.POST.get('answer')  # ユーザーの回答を取得
        # 正解をリストとして取得
        correct_answer = question.get_correct_answer_list()
        # ユーザーの回答をリスト化して正誤を判定
        user_answer_list = user_answer.split(', ')
        if user_answer_list == correct_answer:
            result = "正解です！"
        else:
            result = "不正解です！"
        return render(request, 'quiz/result.html', {'result': result})
    return redirect('quiz:question', pk=pk)
