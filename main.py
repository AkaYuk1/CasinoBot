import asyncio, random, os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("B_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

score = 0

but_red = KeyboardButton(text="красное")
but_white = KeyboardButton(text="белое")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [but_red, but_white],
        [KeyboardButton(text="выйти")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("красное или белое?", reply_markup=keyboard)

@dp.message(F.text.in_({"красное", "белое"}))
async def play(message: Message):
    global score
    choice = random.choice(["красное", "белое"])
    if message.text == choice:
        score += 10
        await message.answer(f"верно: +10$ | balance: {score}$")
    else:
        score -= 10
        await message.answer(f"неверно: -10$ | balance: {score}$")

@dp.message(F.text == "выйти")
async def bue(message: Message):
    await message.answer("вы вышли из игры", reply_markup=ReplyKeyboardRemove())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    