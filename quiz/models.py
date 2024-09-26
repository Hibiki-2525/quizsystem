from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default='default question text') # 問題文
    correct_answer = models.TextField() 

    def __str__(self):
        return self.title

    # 正解をリスト形式で返すヘルパーメソッド
    def get_correct_answer_list(self):
        return self.correct_answer.split('|')  # 区切り文字としてパイプを使用

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)  # ユーザーの答え
    score = models.IntegerField(default=0)  # 点数

