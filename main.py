import os
import asyncio
from aiogram import Bot
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import logging
from dotenv import load_dotenv
from aiogram import Dispatcher

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

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
bt6 = KeyboardButton(text="🛒 Товары")  # Button for products

# Create the main keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [bt1, bt2],
        [bt3, bt6],  # Product button
        [bt4, bt5]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Updated product information
product_info = {
    "Интерактивная панель": {
        "types": {
            "65 Диоганаль": {
                "photo_url": "https://imgur.com/ocU74QJ",
                "description": """
                Активный размер — 2159 х 1215мм; Матрица – DLED; 
                Максимальное разрешение – 3840х2160@60Hz 4К;
                Цвет дисплея – 1,07 Mлрд; Яркость — 350 cd/m; Контрастность — 1200:1/1300:1/3000:1; Углы обзора – 178˚/178˚;
                Сенсор — Инфракрасный до 20 касаний, Время отклика – 7 мс, Соотношение сторон — 16:9;
                Порты: USB 3.0×2, HDMI IN, TOUCH USB, TYPE-C, Keys; Сзади – HDMI INx2, USB 3.0×2, TOUCH USB, RS232,
                USB2.0, AUDIO IN, OPTICAL OUT, LINE OUT, RJ45 IN, RJ45 OUT. Динамики — 2x15W; Связь — 1000М LAN, 
                802.11ac 2.4GHz & 5GHz Wi-Fi; Модуль Android: ОС — Android 14 Интерфейс в 3840х2160. CPU — Quad core A55
                с частотой 1,5 ГГц; GPU — Mali G52MP2; RAM — 4GB, ROM — 32 Gb eMMC. Вес 132 кг; Потребление энергии — 420 Ватт.
                Дизайн: Серебристый металлик."""
            },
            "75 Диоганаль": {
                "photo_url": "https://imgur.com/ocU74QJ",
                "description": """
                Активный размер — 2159 х 1215мм; Максимальное разрешение – 3840х2160@60Hz 4К;
                Цвет дисплея – 1,07 Mлрд; Яркость — 350 cd/m; Контрастность — 1200:1/1300:1/3000:1;
                Углы обзора – 178˚/178˚; Порты: USB 3.0×2, HDMI IN, TOUCH USB, TYPE-C, Keys; Сзади – HDMI INx2, USB 3.0×2, 
                TOUCH USB, RS232, USB2.0, AUDIO IN, OPTICAL OUT, LINE OUT, RJ45 IN, RJ45 OUT. Динамики — 2x15W; Связь — 1000М LAN,
                802.11ac 2.4GHz & 5GHz Wi-Fi. Модуль Android: ОС — Android 14. Вес 132 кг; Дизайн: Серебристый металлик."""
            },
            "86 Диоганаль": {
                "photo_url": "https://imgur.com/ocU74QJ",
                "description": """
                Активный размер — 2159 х 1215мм; Максимальное разрешение – 3840х2160@60Hz 4К;
                Цвет дисплея – 1,07 Mлрд; Яркость — 350 cd/m; Контрастность — 1200:1/1300:1/3000:1;
                Углы обзора – 178˚/178˚; Порты: USB 3.0×2, HDMI IN, TOUCH USB, TYPE-C, Keys; Сзади – HDMI INx2, USB 3.0×2, 
                TOUCH USB, RS232, USB2.0, AUDIO IN, OPTICAL OUT, LINE OUT, RJ45 IN, RJ45 OUT. Динамики — 2x15W; Связь — 1000М LAN,
                802.11ac 2.4GHz & 5GHz Wi-Fi. Модуль Android: ОС — Android 14. Вес 132 кг; Дизайн: Серебристый металлик."""
            }
        }
    },
    "Мобильный стенд": {
        "types": {
            "2000": {
                "photo_url": "https://imgur.com/vY2QcfI",
                "description": """
    Вес: 42kg
    Диапазон наклона: ~ -10° +10°
    Размер панели: 55” – 86 ”
    Габариты: 1640х 900 х 600 мм
    Грузоподъемность: 120kg"""
            },
            "1800": {
                "photo_url": "https://imgur.com/6eKO8cu",
                "description": """
    вес: 180 кг
    Колёсики: Имеются с фиксаторами положения
    Полки: Имеются 2
    Материал: Металл"""
            },
            "1700": {
                "photo_url": "https://imgur.com/4Nk2cRM",
                "description": """
    вес: 100 кг
    Колёсики: Имеются с фиксаторами положения
    Полки: Имеются 2
    Материал: Металл"""
            }
        }
    },
    "Инфокиоск": {
        "types": {
            "32 Диоганаль": {
                "photo_url": "https://imgur.com/DZctjXm",
                "description": """
    Инфокиoск сенсорным экраном.
    Разрешение: 1920x1080
    Подключение: Wi-Fi и Ethernet
    Программное обеспечение: Встраиваемая система 
    Android
    Материал: Металл и стекло
    Применение: Информация, реклама, интерактивные 
    функции."""
            },
            "43 Диоганаль": {
                "photo_url": "https://imgur.com/ukaJTeQ",
                "description": """
    Инфокиoск сенсорным экраном.
    Разрешение: 1920x1080
    Подключение: Wi-Fi и Ethernet
    Программное обеспечение: Встраиваемая система 
    Android
    Материал: Металл и стекло
    Применение: Информация, реклама, интерактивные 
    функции."""
            },
            "55 Диоганаль": {
                "photo_url": "https://imgur.com/Yu9LzwC",
                "description": """
    Инфокиoск сенсорным экраном.
    Разрешение: 1920x1080
    Подключение: Wi-Fi и Ethernet
    Программное обеспечение: Встраиваемая система 
    Android
    Материал: Металл и стекло
    Применение: Информация, реклама, интерактивные 
    функции."""
            }
        }
    }
} 
# Product type keyboard (inline)
def get_type_keyboard(product_name):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for type_name in product_info[product_name]["types"].keys():
        button = InlineKeyboardButton(text=type_name, callback_data=f"{product_name}:{type_name}")
        keyboard.inline_keyboard.append([button])
    # Add back button to return to product selection
    back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_products")
    keyboard.inline_keyboard.append([back_button])
    return keyboard

# Main /start handler
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=main_keyboard)

# Show products list
@dp.message(lambda message: message.text == "🛒 Товары")
async def show_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for product_name in product_info.keys():
        button = InlineKeyboardButton(text=product_name, callback_data=product_name)
        keyboard.inline_keyboard.append([button])
    await message.answer("Выберите товар:", reply_markup=keyboard)

# Show product types when a product is selected
@dp.callback_query(lambda call: call.data in product_info.keys())
async def show_product_types(callback_query: types.CallbackQuery):
    product_name = callback_query.data
    await callback_query.message.edit_text(f"Выберите тип для {product_name}:", reply_markup=get_type_keyboard(product_name))

# Send product info when a type is selected
@dp.callback_query(lambda call: ":" in call.data)
async def send_product_info(callback_query: types.CallbackQuery):
    product_name, type_name = callback_query.data.split(":")
    product_type = product_info[product_name]["types"][type_name]

    await bot.send_photo(
        chat_id=callback_query.message.chat.id,
        photo=product_type["photo_url"],
        caption=f"{product_name} - {type_name}\n\n{product_type['description']}",
        reply_markup=get_type_keyboard(product_name)  # Include back button here as well
    )

# Back to product types from product info
@dp.callback_query(lambda call: call.data == "back_to_products")
async def back_to_products(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await show_products(callback_query.message)

# Main entry point
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
