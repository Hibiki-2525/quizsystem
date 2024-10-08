from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
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
    cards = question.cards.all()  # カードを取得
    return render(request, 'quiz/question.html', {'question': question, 'cards': cards})

# 回答送信
#def submit_answer(request, pk):
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

# 回答送信
#def submit_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        user_answer = request.POST.get('answer')  # ユーザーの回答を取得
        correct_answer = question.get_correct_answer_list()  # 正解をリストとして取得
        user_answer_list = user_answer.split(', ')  # ユーザーの回答をリスト化

        # 各行ごとの正誤判定
        result_list = []
        for user_ans, correct_ans in zip(user_answer_list, correct_answer):
            if user_ans == correct_ans:
                result_list.append('◯')
            else:
                result_list.append('✕')

        # 3つのリストをまとめたリストを作成
        combined_list = zip(user_answer_list, correct_answer, result_list)

        # 行ごとの判定結果をテンプレートに渡す
        return render(request, 'quiz/result.html', {
            'combined_list': combined_list
        })

    return redirect('quiz:question', pk=pk)


#def submit_answer(request, pk):
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

        # 次の問題を取得
        try:
            next_question = Question.objects.filter(pk__gt=question.pk).order_by('pk').first()
            if next_question:
                return redirect('quiz:question', pk=next_question.pk)
            else:
                return render(request, 'quiz/result.html', {'result': result, 'user_answer': user_answer_list, 'correct_answer': correct_answer})
        except Question.DoesNotExist:
            return redirect('quiz:home')  # エラーの場合もホームにリダイレクト

    return redirect('quiz:question', pk=pk)


# 回答送信
def submit_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == 'POST':
        user_answer = request.POST.get('answer')  # ユーザーの回答を取得
        # 正解をリストとして取得
        correct_answer = question.get_correct_answer_list()
        # ユーザーの回答をリスト化して正誤を判定
        user_answer_list = user_answer.split(', ')
        # デバッグ用出力
        print("正解:", correct_answer)
        print("ユーザーの回答:", user_answer_list)
        is_correct = (user_answer_list == correct_answer)

        # セッションに問題番号と正誤を記録する
        if 'results' not in request.session:
            request.session['results'] = []
        
        request.session['results'].append({
            'question_number': question.pk,
            'result': '正解' if is_correct else '不正解'
        })
        request.session.modified = True

        # 次の問題を取得
        next_question = Question.objects.filter(pk__gt=question.pk).order_by('pk').first()
        if next_question:
            # 次の問題がある場合はその問題にリダイレクト
            return redirect('quiz:question', pk=next_question.pk)
        else:
            # 次の問題がない場合は結果画面にリダイレクト
            return redirect('quiz:result')  # 結果画面にリダイレクト

    return redirect('quiz:question', pk=pk)

# 結果画面
def result_view(request):
    results = request.session.get('results', [])
    return render(request, 'quiz/result.html', {'results': results})
