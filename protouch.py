import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Define buttons with emojis
bt1 = KeyboardButton(text="🏢 О нас")
bt2 = KeyboardButton(text="💬 Обратная связь")
bt3 = KeyboardButton(text="📋 Вакансии")
bt4 = KeyboardButton(text="📞 Контакты")
bt5 = KeyboardButton(text="🇷🇺/🇺🇿 Сменить язык")
bt6 = KeyboardButton(text="🔙 Назад")
bt7 = KeyboardButton(text="🛒 Товары")  # Button for products

# Create the main keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [bt1, bt2],
        [bt3, bt7],  # Product button
        [bt4, bt5]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Create the products keyboard
products_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Интерактивная панель"), KeyboardButton(text="Моноблок")],
        [KeyboardButton(text="Камера"), KeyboardButton(text="Инфокiosk")],
        [bt6]  # Back button
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# User data storage (consider using a more robust solution for real apps)
user_data = {}

# Handle /start and /help commands
@dp.message(Command(commands=['start', 'help']))
async def welcome(message: types.Message):
    await message.answer("Здравствуйте! Добро пожаловать в наш бот!", reply_markup=main_keyboard)

# Handle incoming messages
@dp.message()
async def handle_message(message: types.Message):
    global user_data

    if message.text == '🏢 О нас':
        await message.answer("«ProTouch» — дистрибьютор профессионального аудио и видео оборудования.", reply_markup=main_keyboard)
    elif message.text == '💬 Обратная связь':
        await message.answer("ProTouch.uz@gmail.com\nhttps://t.me/protouchuzb", reply_markup=main_keyboard)
    elif message.text == '📋 Вакансии':
        await message.answer("Пожалуйста, выберите одну из следующих кнопок:", reply_markup=main_keyboard)
    elif message.text == '📞 Контакты':
        await message.answer("+998974330303; +998951937700\n9:00 - 18:00\nАдрес: Asaka-street 35, 700100, Ташкент", reply_markup=main_keyboard)
    
    # Handle product selection
    elif message.text == '🛒 Товары':
        await message.answer("Пожалуйста, выберите товар:", reply_markup=products_keyboard)
    
    # Handle product choice
    elif message.text in ["Интерактивная панель", "Моноблок", "Камера", "Инфокiosk"]:
        user_data['product'] = message.text  # Save selected product
        await message.answer(f"Вы выбрали товар: {message.text}. Сколько нужно? Введите количество:", reply_markup=main_keyboard)
        user_data['step'] = 'waiting_for_quantity'  # Update user state
    
    # Handle quantity input
    elif user_data.get('step') == 'waiting_for_quantity':
        try:
            quantity = int(message.text)
            user_data['quantity'] = quantity
            await message.answer("Введите ваше имя:", reply_markup=main_keyboard)
            user_data['step'] = 'waiting_for_name'
        except ValueError:
            await message.answer("Пожалуйста, введите правильное количество:", reply_markup=main_keyboard)
    
    # Handle name input
    elif user_data.get('step') == 'waiting_for_name':
        user_data['name'] = message.text
        await message.answer("Введите вашу фамилию:", reply_markup=main_keyboard)
        user_data['step'] = 'waiting_for_surname'
    
    # Handle surname input
    elif user_data.get('step') == 'waiting_for_surname':
        user_data['surname'] = message.text
        await message.answer("Введите ваш номер телефона:", reply_markup=main_keyboard)
        user_data['step'] = 'waiting_for_phone'
    
    # Handle phone number input
    elif user_data.get('step') == 'waiting_for_phone':
        user_data['phone'] = message.text
        await message.answer("Спасибо за вашу информацию! Мы свяжемся с вами в ближайшее время.", reply_markup=main_keyboard)

        # Optionally reset user data or state here
        user_data.clear()  # Clear user data after processing the order

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))