import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from User import *

user=UserList()
bot = Bot(token="your token")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#Handler for follow new users in chat and check if user in db or not
@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message):
    if user.Check_User(message.from_user.id)==False:
        user_name = message.from_user.first_name
        keyboard = InlineKeyboardMarkup()
        layer = ["Бот", "Человек", "Вомбат", "Дракон", "Утка"]
        random.shuffle(layer)
        for i in layer:
            if i == "Человек":
                keyboard.add(InlineKeyboardButton(i, callback_data=2))
            else:
                keyboard.add(InlineKeyboardButton(i, callback_data=1))
        await bot.send_message(message.chat.id, "Привет, {0}!\nТы кто ???".format(user_name), reply_markup=keyboard)
        await message.chat.restrict(
            message.from_user.id, permissions=types.ChatPermissions(can_send_messages=False)
        )
    else:
        await bot.send_message(message.chat.id,"Рад видеть тебя снова!")


#Handler for work with callback query check if answer true or not
@dp.callback_query_handler(lambda c: c.data)
async def process_callback_private(callback_query: types.CallbackQuery):
    if user.Check_User(callback_query.from_user.id)==False:
        if callback_query.data!="2":
            await callback_query.answer(("Ты ошибся.."), show_alert=True)
            await asyncio.sleep(2)
            await callback_query.message.chat.kick(callback_query.from_user.id)
            await callback_query.message.chat.unban(callback_query.from_user.id)
        else:
            await callback_query.answer(("Правильный ответ!"))
            user.Save(callback_query.from_user.id)
            await callback_query.message.chat.restrict(callback_query.from_user.id, permissions=types.ChatPermissions(can_send_messages=True))
            await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
        executor.start_polling(dp,skip_updates=True)