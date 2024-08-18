from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)

helper = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='Чем я могу вам помочь?',
    keyboard=[
        [KeyboardButton(text='Не работает домофон')],
        [KeyboardButton(text='Не работает камера')],
        [KeyboardButton(text='Проблемы с магнитом')],
        [KeyboardButton(text='Проблема с доводчиком')],
        [KeyboardButton(text='Проблема с кнопкой выхода')],
        [KeyboardButton(text='Закончились чип ключи')],
    ]
)


intercom = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='С чем именно у вас возникли сложности?',
    keyboard=[
        [KeyboardButton(text='Не распознаванает')],
        [KeyboardButton(text='Не работает Удаленный доступ (Открытие двери через приложение)')],
        [KeyboardButton(text='Не работает Камера домофона')],
        [KeyboardButton(text='Не приходят звоноки')],
        [KeyboardButton(text='Не горит экран или клавиатура')],
        [KeyboardButton(text='Не работают чипы')],
    ]
)

magnit = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='С чем именно у вас возникли сложности?',
    keyboard=[
        [KeyboardButton(text='Не закреплен')],
        [KeyboardButton(text='Не работает')],
        [KeyboardButton(text='Слабо держит')],
    ]
)

hand = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='С чем именно у вас возникли сложности?',
    keyboard=[
        [KeyboardButton(text='Скрипит')],
        [KeyboardButton(text='Не закрывается')],
        [KeyboardButton(text='Хлопает')],
        [KeyboardButton(text='Слишком тяжело открывается дверь')],
        [KeyboardButton(text='Нет болта')],
        [KeyboardButton(text='Сломан')],
    ]
)

ex_button = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='С чем именно у вас возникли сложности?',
    keyboard=[
        [KeyboardButton(text='Не работает')],
    ]
)

camera = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder='С чем именно у вас возникли сложности?',
    keyboard=[
        [KeyboardButton(text='Плохое изображение')],
        [KeyboardButton(text='Камера не держит (упала)')],
    ]
)

ok = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[
        [KeyboardButton(text='Правильно')],
        [KeyboardButton(text='Отмена')],
    ]
)


report = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[
        [KeyboardButton(text='/report')],
    ]
)

cancel = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[
        [KeyboardButton(text='Отмена')],
    ]
)