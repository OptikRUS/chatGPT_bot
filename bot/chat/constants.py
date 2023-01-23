from random import choice

from ..keyboards import ChatButtons

MAIN_MENU_MESSAGE: str = "Главное меню 📎"
WAIT_CODE: str = "⏳ Генерация кода..."
WAIT_TEXT: str = "⏳ Генерация текста..."
WAIT_IMAGE: str = "⏳ Генерация изображения..."
WRONG_INPUT: str = "Некорректный ввод. Введите валидный текст."

GENERATE_IMAGE_BUTTON: str = ChatButtons.generate_image.name
GENERATE_TEXT_BUTTON: str = ChatButtons.generate_text.name
GENERATE_CODE_BUTTON: str = ChatButtons.generate_code.name

UNSAFE_REQUEST: str = f"""
⚠️ Ваш запрос был отклонен из-за системы безопасности.\n
❗Это может быть вызвано запросом, содержащим  насилие, терроризм, дискриминацию, нецензурную лексику, порнографию, оскорбления или другие материалы, которые могут навредить другим людям или нарушить законы.
"""


REMEMBER: str = """
Помните, чем более конкретно и ясно вы формулируете запрос, тем лучше результат генерации текста будет соответствовать вашим ожиданиям.\n
"""

IMAGE_GENERATION_REQUEST_EXAMPLES: tuple = (
    "Создайте изображение красивой девушки на пляже",
    "Сгенерируйте изображение горной дороги в зимний день",
    "Создайте изображение красивой девушки на пляже",
    "Сгенерируйте изображение горной дороги в зимний день",
    "Создайте изображение ночного города с видом на звезды",
    "Создайте изображение суперкара на автостраде",
    "Создайте изображение детской комнаты с игрушками"
)

TEXT_GENERATION_REQUEST_EXAMPLES: tuple = (
    "Расскажите о последних новостях в мире технологий",
    "Напишите статью о преимуществах использования возобновляемых источников энергии",
    "Расскажите о главных событиях в истории страны",
    "Напишите рецензию на последний фильм, который вы посмотрели",
    "Расскажите о своем любимом городе"
)

CODE_GENERATION_REQUEST_EXAMPLES: tuple = (
    "Напишите код на Python, который считывает данные из CSV-файла и выводит сумму всех чисел в столбце 'Total'",
    "Напишите Python функцию, которая принимает список слов и возвращает самое длинное слово в списке",
    "Напишите код на Python, который преобразует строку в формат JSON",
    "Напишите Python скрипт, который подключается к БД, выбирает данные из таблицы 'orders' и выводит их в терминал",
    "Напишите Python класс, который реализует стек и его основные методы (push, pop, peek)",
    "Напишите Python функцию, которая принимает список чисел и возвращает сумму всех чисел в списке"
    "Напишите Python класс, который представляет книгу, с методами для получения названия, автора и количества страниц",
    "Напишите Python скрипт, который ищет все файлы с расширением .txt в директории и выводит их имена на экран",
    "Напишите Python функцию, которая принимает строку и возвращает True, если строка является палиндромом, иначе False",
    "Напишите Python код, который соединяет два списка используя оператор +",
    "Напишите функцию для сортировки массива на Python с использованием алгоритма пузырька",
    "Создайте класс для работы с базой данных MySQL на Python",
    "Напишите скрипт для автоматического отправления электронной почты с использованием smtplib в Python"
)


def image_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(IMAGE_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации изображения:
    """
    return message


def text_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(TEXT_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации текста:
    """
    return message


def code_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(CODE_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации кода:
    """
    return message
