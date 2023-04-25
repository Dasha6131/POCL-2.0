'''Тесты для проекта'''
from app import classify


def test_classify():
    """Classify the given text using a classifier"""
    answer = classify(
        "Добрый вечер! Не могу зайти в личный кабинет."
        " Предполагаю, что я не зарегистрированный пользователь."
        " Помогите, пожалуйста, разобраться.?")
    assert answer[1] > 0.8 and answer[0] == 'Учетная запись'


def test_classify2():
    """Classify the given text using a classifier"""
    answer = classify(
        "Здравствуйте! Не могу понять как правильно сделать"
        " рабочую программу дисциплины в программе, как мне это сделать?")
    assert answer[1] > 0.9 and answer[0] == 'Учебные планы'


def test_classify3():
    """Classify the given text using a classifier"""
    answer = classify(
        "Психологический, группа OZ1121 Добрый день!"
        " Обращаюсь к вам с просьбой о создании корпоративной почты,"
        " с целью дальнейшей работы в системе Moodle и Teams.")
    assert answer[1] > 0.7 and answer[0] == 'Учетная запись'
