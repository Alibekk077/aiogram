import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
TOKEN ="1932873930:AAFAlpFzzXzNU-1cAe-eBIpsHhf6PYI5z9o"
my_id = 730053486

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="salam ")

@dp.message_handler()
async def echo(message: Message):
    text = f"Aleke: {message.text}"
    await bot.send_message(chat_id=message.from_user.id,
                          text=text)
if __name__ == "__main__":
     executor.start_polling(dp, on_startup=send_to_admin)