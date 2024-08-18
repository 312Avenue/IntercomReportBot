import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import FSInputFile
from aiogram.filters import CommandStart, Command

import keyboards as kb
import commands as cm
import bx_logic as bx24


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуйте, здесь вы можете оставить заявку', reply_markup=kb.report)
    

@router.message(F.text == 'Отмена')
async def cancel_action(message: Message):
    await message.answer('Действие отменено', reply_markup=kb.report)


@router.message(Command('report'))
async def report(message: Message):
    user = message.from_user.id
    text = 'Напишите ФИО'
    
    cm.upsert_user_state(user, 1)
    await message.answer('Напишите ФИО')
    

@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 1)
async def handle_name(message: Message):
    user = message.from_user.id
    mes = message.text

    cm.upsert_ticket(user, 'name', mes)
    cm.upsert_user_state(user, 2)

    await message.answer('Напишите  номер телефона.\nНомер в виде: 707901091', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 2)
async def handle_num(message: Message):
    user = message.from_user.id
    mes = message.text
    
    if len(mes) > 9:
        cm.upsert_user_state(user, 1)
        await message.answer('Напишите  номер телефона для связи.\nНомер в виде: 707901091', reply_markup=kb.cancel)    
    else:
        cm.upsert_ticket(user, 'num', mes)
        cm.upsert_user_state(user, 3)

        await message.answer('Напишите ваш адрес.\nАдрес в качестве примера:\n12 мкрн. 12/1 дом\nул. Кулатова 14 дом', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 3)
async def handle_addr(message: Message):
    user = message.from_user.id
    mes = message.text

    cm.upsert_ticket(user, 'address', mes)
    cm.upsert_user_state(user, 4)

    await message.answer('Напишите номер подъезда (Числом)', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 4)
async def handle_enter(message: Message):
    user = message.from_user.id
    mes = message.text
    
    if mes.isdigit():
        cm.upsert_ticket(user, 'enter', mes)
        cm.upsert_user_state(user, 5)

        await message.answer('Что случилось?', reply_markup=kb.helper)
    else:
        cm.upsert_user_state(user, 3)
        await message.answer('Напишите номер подъезда (Числом)', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 5)
async def handle_problem(message: Message):
    user = message.from_user.id
    mes = message.text

    cm.upsert_ticket(user, 'problem', mes)
    cm.upsert_user_state(user, 6)

    if mes == 'Не работает домофон':
        await message.answer('С чем именно у вас возникли сложности?', reply_markup=kb.intercom)
    elif mes == 'Не работает камера':
        await message.answer('С чем именно у вас возникли сложности?', reply_markup=kb.camera)
    elif mes == 'Проблемы с магнитом':
        await message.answer('С чем именно у вас возникли сложности?', reply_markup=kb.magnit)
    elif mes == 'Проблема с доводчиком':
        await message.answer('С чем именно у вас возникли сложности?', reply_markup=kb.hand)
    elif mes == 'Проблема с кнопкой выхода':
        await message.answer('С чем именно у вас возникли сложности?', reply_markup=kb.ex_button)
    elif mes == 'Закончились чип ключи':
        await message.answer('Напишите количество чипов', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 6)
async def handle_opt_probl(message: Message):
    user = message.from_user.id
    mes = message.text

    cm.upsert_ticket(user, 'option_problem', mes)
    cm.upsert_user_state(user, 7)
    
    await message.answer('Напишите комментарий', reply_markup=kb.cancel)


@router.message(lambda message: cm.get_user_state(message.from_user.id)[0] == 7)
async def handle_opt_probl(message: Message):
    user = message.from_user.id
    mes = message.text

    cm.upsert_ticket(user, 'description', mes)
    cm.upsert_user_state(user, 8)
    data = cm.get_ticket(user)
    
    await message.answer(f'Проверьте данные:\nФИО: {data[0]}\nНомер телефона: {data[1]}\
        \n{data[2]}\nПодъезд: {data[3]}\nТип обращения: {data[5]}\
        \nДополнителья информация: {data[6]}\nКомментарий: {data[7]}', reply_markup=kb.ok)
    

@router.message(F.text == 'Правильно')
async def handle_opt_probl(message: Message):
    user = message.from_user.id
    data = cm.get_ticket(user)
    
    await bx24.push_bx(data)
    await message.answer('Заявка оформлена, в ближайшее время с вами свяжутся наши специалисты', reply_markup=kb.report)
    
    
@router.message(F.text == 'Отмена')
async def handle_opt_probl(message: Message):
    await message.answer('Начни оформление', reply_markup=kb.report)
    