from .models import Question, Card
import os
import random

def generate_cards_from_db(question_id):
    # Questionモデルから正解コードを取得
    question = Question.objects.get(pk=question_id)
    correct_code = question.correct_code

    # 正解コードからダミーコードを生成し、カードを作成
    correct_lines = correct_code.strip().split('\n')
    dummy_code = generate_dummy_code(correct_lines)

    # 正解コードとダミーコードを組み合わせてシャッフル
    combined_lines = correct_lines + dummy_code
    random.shuffle(combined_lines)

    # カードをデータベースに保存
    for line in combined_lines:
        Card.objects.create(question=question, card_text=line)

    print(f"Cards created for question {question_id}")

def generate_dummy_code(correct_lines, num_dummy_lines=3):
    dummy_lines = []
    variables = set()
    contains_for = False
    contains_if = False
    contains_while = False

    for line in correct_lines:
        if '=' in line:
            var = line.split('=')[0].strip()
            variables.add(var)
        if 'for' in line:
            contains_for = True
        if 'if' in line:
            contains_if = True
        if 'while' in line:
            contains_while = True

    for _ in range(num_dummy_lines):
        var1 = random.choice(list(variables))
        var2 = random.choice(list(variables))
        operation = random.choice(['+', '-', '*', '/'])
        dummy_line = f"{var1} = {var1} {operation} {var2}"
        dummy_lines.append(dummy_line)

    # Generate appropriate dummy control structures
    if contains_for:
        var1 = random.choice(list(variables))
        var2 = random.choice(list(variables))
        operation = random.choice(['+', '-', '*', '/'])
        dummy_lines.append(f"for {var} in {var}+1:")
    if contains_if:
        var = random.choice(list(variables))
        condition_value = random.choice(list(variables) + [str(random.randint(-10, 10))])
        condition = random.choice([f"{var} > {condition_value}", f"{var} < {condition_value}", f"{var} == {condition_value}"])
        dummy_lines.append(f"if {condition}:")
    if contains_while:
        var = random.choice(list(variables))
        dummy_lines.append(f"while {var} < 10:\n    {var} += 1")

    return dummy_lines

