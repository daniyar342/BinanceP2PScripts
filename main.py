# #
# # TELEGRAM_BOT_TOKEN = os.environ.get('5632390525:AAES0jF_myBdjdapYBjkvXPhYafmfB0W7D0')
# # # Устанавливаем ключ API Binance
# # BINANCE_API_KEY = os.environ.get('NzrqoofL8zudNGnq2TcaRa0jy7GR8cyrE6mMqagbJbTQN0pooC8IdWwXOQZZuosf')
# # BINANCE_SECRET_KEY = os.environ.get('kr5egGS25YEmeCOn3eGL3nZD1rfztagzaHQCJNBLp6orQaYE76CyAypuLTSgAtX2')
#
# import os
# import requests
# import asyncio
# import logging
#
#
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
# from aiogram.utils import executor
#
#
# # Устанавливаем ключ API Telegram
# TELEGRAM_BOT_TOKEN = os.environ.get('5632390525:AAES0jF_myBdjdapYBjkvXPhYafmfB0W7D0')
#
# # Устанавливаем ключ API Binance
# BINANCE_API_KEY = os.environ.get('NzrqoofL8zudNGnq2TcaRa0jy7GR8cyrE6mMqagbJbTQN0pooC8IdWwXOQZZuosf')
# BINANCE_SECRET_KEY = os.environ.get('kr5egGS25YEmeCOn3eGL3nZD1rfztagzaHQCJNBLp6orQaYE76CyAypuLTSgAtX2')
#
#
# # Создаем объекты бота и диспетчера
# bot = Bot(token="5632390525:AAES0jF_myBdjdapYBjkvXPhYafmfB0W7D0")
# dp = Dispatcher(bot)
#
#
# # Создаем обработчик команды /start
# @dp.message_handler(commands=['start'])
# async def start_command_handler(message: types.Message):
#     # Создаем список кнопок с валютами, для которых хотим получить данные
#     buttons = [
#         InlineKeyboardButton('USDT/KGS', callback_data='KGS'),
#         InlineKeyboardButton('USDT/KZT', callback_data='KZT'),
#         InlineKeyboardButton('USDT/RUB', callback_data='RUB'),
#         InlineKeyboardButton('USDT/PLN', callback_data='PLN')
#     ]
#
#     # Создаем разметку с кнопками
#     reply_markup = InlineKeyboardMarkup(row_width=2)
#     reply_markup.add(*buttons)
#
#     # Отправляем сообщение с разметкой в чат
#     await bot.send_message(chat_id=message.chat.id, text='Выберите валюту:', reply_markup=reply_markup)
#
#
# # Создаем обработчик нажатия на кнопку в разметке
# @dp.callback_query_handler()
# async def button_callback_handler(callback_query: CallbackQuery):
#     try:
#         # Получаем данные о выбранной валюте
#         currency = callback_query
#
#         # Получаем цену USDT для выбранной валюты через API Binance
#         endpoint = 'https://api.binance.com/sapi/v1//fiat/orders'
#         payload = {
#             'asset': 'USDT',
#             'fiat': currency,
#             'side': 'BUY',
#             'type': 'SPOT',
#             'transType': 'P2P',
#             'page': 1,
#             'rows': 1
#         }
#         headers = {
#             'X-MBX-APIKEY': BINANCE_API_KEY
#         }
#         response = requests.get(endpoint, params=payload, headers=headers).json()
#         price = response['data'][0]['price']
#
#         # Отправляем сообщение с информацией о цене в чат
#         await bot.edit_message_text(chat_id=callback_query.message.chat.id,
#                                     message_id=callback_query.message.message_id,
#                                     text=f"Цена USDT для {currency}: {price} {currency}")
#     except Exception as e:
#         logging.error(e)
#         await bot.answer_callback_query(callback_query.id, text='Что-то пошло не так...')
#
#
# if __name__ == '__main__':
#     # Запускаем бота
#     executor.start_polling(dp, skip_updates=True)

# import requests
# import json
# import hashlib
# import hmac
# import time
#
# api_key = "NzrqoofL8zudNGnq2TcaRa0jy7GR8cyrE6mMqagbJbTQN0pooC8IdWwXOQZZuosf"
# secret_key = b"kr5egGS25YEmeCOn3eGL3nZD1rfztagzaHQCJNBLp6orQaYE76CyAypuLTSgAtX2"
#
# def get_binance_p2p_trades(symbol, limit=500):
#     endpoint = "https://api.binance.com/sapi/v1/c2c/orderMatch/listUserOrderHistory"
#     timestamp = int(time.time() * 1000)
#     querystring = f"symbol={symbol}&limit={limit}&timestamp={timestamp}"
#     signature = hmac.new(secret_key, querystring.encode("utf-8"), hashlib.sha256).hexdigest()
#
#     headers = {
#         "X-MBX-APIKEY": api_key
#     }
#
#     url = f"{endpoint}?{querystring}&signature={signature}"
#
#     response = requests.get(url, headers=headers)
#     data = json.loads(response.text)
#
#     return data
# trade = get_binance_p2p_trades("USDTRUB",limit=50)
# print(trade["data"])
#
# import hashlib
# import hmac
# import requests
# import time
#
# api_key = 'NzrqoofL8zudNGnq2TcaRa0jy7GR8cyrE6mMqagbJbTQN0pooC8IdWwXOQZZuosf'
# api_secret = b"kr5egGS25YEmeCOn3eGL3nZD1rfztagzaHQCJNBLp6orQaYE76CyAypuLTSgAtX2"
#
# def get_binance_p2p_ticker(symbol):
#     url = "https://api.binance.com/sapi/v1/p2p/orderbook/ticker"
#     querystring = {"symbol": symbol}
#     timestamp = int(time.time() * 1000)
#     querystring.update({"timestamp": timestamp})
#     signature = hmac.new(api_secret, str(querystring).encode('utf-8'), hashlib.sha256).hexdigest()
#     headers = {
#         'X-MBX-APIKEY': api_key
#     }
#     querystring.update({"signature": signature})
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     return response.json()
# TRADE = get_binance_p2p_ticker("BTCUSDT")
# print(TRADE)

import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "YOUR_API_KEY"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["rates"][target_currency]
    else:
        return None

