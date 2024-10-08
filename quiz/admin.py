from django.contrib import admin
from .models import Question, Card

class CardInline(admin.TabularInline):  # or admin.StackedInline
    model = Card
    extra = 1  # 新規作成フォームをいくつ表示するか（1つでよい場合）

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'correct_answer')  # 一覧表示でのカラム
    inlines = [CardInline]  # Card をインラインで追加

