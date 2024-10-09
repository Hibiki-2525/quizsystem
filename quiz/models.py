from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)  # 問題のタイトル（例：問1）
    text = models.TextField()  # 問題文を保存
    correct_code = models.TextField()  # 正解のコード（複数行で保存）

    def get_correct_answer_list(self):
        # 正解コードを行ごとに分割してリストにする
        return self.correct_code.strip().split('\n')

    
def generate_cards_from_code(correct_code):
    lines = correct_code.strip().split('\n')  # コードを行ごとに分割
    return lines


class Card(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='cards')  # ここでrelated_nameを追加
    card_text = models.CharField(max_length=255)  # カードに表示するコードの一部



class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)  # ユーザーの答え
    score = models.IntegerField(default=0)  # 点数

