from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

TOKEN = "8000497125:AAFluNimsudiEEcqbayveAMgS_pydKbEbDM"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())


def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="📅 Расписания", url="https://example.com/raspisanie")
    kb.button(text="🌐 Соц. сети", callback_data="social")
    kb.button(text="🌍 Наш сайт", url="https://example.com")
    kb.button(text="🛠 Тех поддержка", callback_data="support")
    kb.adjust(1)
    return kb.as_markup()

def social_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="TikTok", url="https://example.com/tiktok")
    kb.button(text="Instagram", url="https://example.com/insta")
    kb.button(text="YouTube", url="https://example.com/youtube")
    kb.button(text="Facebook", url="https://example.com/facebook")
    kb.button(text="🔙 Назад", callback_data="back")
    kb.adjust(1)
    return kb.as_markup()

async def start_handler(message: types.Message):
    await message.answer("Здравствуйте, дорогой посетитель! Чем могу вам помочь?", reply_markup=main_menu())

async def show_social_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Наши соц. сети:", reply_markup=social_menu())

async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text("Чем ещё могу помочь?", reply_markup=main_menu())

async def support_message(callback: types.CallbackQuery):
    await callback.message.edit_text("Сейчас техническая поддержка недоступна.")
    await asyncio.sleep(2)
    await callback.message.edit_text("Чем ещё могу помочь?", reply_markup=main_menu())

def register_handlers():
    dp.message.register(start_handler, F.text == "/start")
    dp.callback_query.register(show_social_menu, F.data == "social")
    dp.callback_query.register(back_to_main, F.data == "back")
    dp.callback_query.register(support_message, F.data == "support")

async def main():
    register_handlers()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
