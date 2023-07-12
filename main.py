from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
from sql import sql_query, sql_quey, sql_quey_complaint_set
import re


def word_verification(word):
    if sql_quey(word) == None:
        word = '<b>Данный запрос не распознан.</b>' + '\n' + \
               'используйте мои знания как словарь. Вы мне словао, например, ' + '\n' + \
               '<code>База знаний</code>, (синий текст кликабелен)' + '\n' + ' а я в ответ определение этого слова'
    else:
        qwery = sql_quey(word)
        list_str = qwery.split("<br>")
        word = ''
        for i in list_str:
            word = word + i + '\n'

    return word


def word_split_lower(word):
    # убрать все лишние символы
    word = re.sub('\s+|\n|\r|\s+$', ' ', word).strip().lower()
    return word
fff=1

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
HELP_COMMAND = """
/start - начало работы с ботом
/help - список команд
"""

ggg = 2


# Приветствие
@dp.message_handler(commands=['start'])
async def comand_start(message: types.Message):
    user_first_name = message.from_user.first_name
    await message.answer(
        text='Добро пожаловать, ' + user_first_name + '\n'
             + '<code>База знаний</code>, спроси у меня это определение' + '\n'
             + '(выделеннный текст кликабелен)',
        parse_mode="HTML")


@dp.message_handler(commands=['help'])
async def comand_start(message: types.Message):
    if message.from_user.id == 0:
        data = sql_quey_complaint_set()
        for i in data:
            await message.answer(text=i[0])
    else:
        await message.answer(text=HELP_COMMAND)


@dp.message_handler()
async def any_text_message(message: types.Message):
    word = word_split_lower(message.text)
    word = word_verification(word)
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_username = message.from_user.username
    sql_query(user_id, user_first_name, user_last_name, user_username, word)

    await message.answer(word, parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp)
