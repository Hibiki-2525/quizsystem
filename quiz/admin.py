from django.contrib import admin
from .models import Question, Card
from .models import generate_cards_from_code

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'correct_code')
    inlines = [CardInline]  # Card をインラインで追加

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # 正解コードからカードを生成
        cards = generate_cards_from_code(obj.correct_code)

        # 古いカードを削除して新しく生成したカードを保存
        Card.objects.filter(question=obj).delete()  # 重複を避けるために既存のカードを削除
        for card_text in cards:
            Card.objects.create(question=obj, card_text=card_text)
