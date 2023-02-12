from aiogram import Bot, Dispatcher, executor, types
import logging
import pars
import my_token

bot = Bot(my_token.TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/Dollar_USA', '/Dollar_Australian', '/Dollar_Canadian', '/Euro', '/GBP', '/China_yuan', '/Japan_yen', '/Belarus_rub', '/Dollar_Singapore']
    keyboard.add(*buttons)
    await message.answer("Hello.\nКурс какой валюты показать?",reply_markup=keyboard)


@dp.message_handler(commands='Dollar_USA')
async def dollar(message: types.Message):
    await message.answer(f'Доллар США:\n{pars.dollar()}\nИзменился на:{pars.dollar_change()}')
    
@dp.message_handler(commands='Dollar_Australian')
async def Australian_dollar(message: types.Message):
    await message.answer(f'Австралийский доллар:\n{pars.Australian_dollar()}\nИзменился на:{pars.Australian_dollar_change()}')

@dp.message_handler(commands='Dollar_Canadian')
async def Canadian_dollar(message: types.Message):
    await message.answer(f'Канадский доллар:\n{pars.Canadian_dollar()}\nИзменился на:{pars.Canadian_dollar_change()}')


@dp.message_handler(commands='Euro')
async def euro(message: types.Message):
    await message.answer(f'Евро:\n{pars.euro()}\nИзменился на:{pars.euro_change()}')

@dp.message_handler(commands='GBP')
async def GBP(message: types.Message):
    await message.answer(f'Фунт стерлингов\nСоединенного королевства:\n{pars.GBP()}\nИзменился на:{pars.GBP_change()}')

@dp.message_handler(commands='belarus_rub')
async def belarus_rub(message: types.Message):
    await message.answer(f'Беларусский рубль:\n{pars.belarussian_ruble()}\nИзменился на:{pars.belarussian_ruble_change()}')


@dp.message_handler(commands='China_yuan')
async def yuan(message: types.Message):
    await message.answer(f'Китайский юань:\n{pars.yuan()}\nИзменился на:{pars.yuan_change()}')

@dp.message_handler(commands='Japan_yen')
async def yen(message: types.Message):
    await message.answer(f'Японская иена:\n{pars.yen()}\nИзменился на:{pars.yen_change()}')

@dp.message_handler(commands='Dollar_Singapore')
async def dollar(message: types.Message):
    await message.answer(f'Доллар Сингапурский:\n{pars.Singapore_dollar()}\nИзменился на:{pars.Singapore_dollar_change()}')


executor.start_polling(dp, skip_updates=True)