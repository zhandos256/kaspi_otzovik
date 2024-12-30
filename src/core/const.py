import textwrap
from pathlib import Path

from aiogram.types import BotCommand

DEBUG = 0

TOKEN = "7692919718:AAH0myJyR66DbGjQvc9Bl1YBeCHOl-nnyjs"

BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
DB_FILE_PATH = BASE_DIR / 'db.sqlite'
DB_URL = f'sqlite+aiosqlite:///{DB_FILE_PATH}'

BOT_COMMANDS = [
    BotCommand(command='/start', description='start command'),
    BotCommand(command='/help', description='help command'),
]

DEFAULT_TEMPLATE_MSG = textwrap.dedent("""
    Здравстуйте 👋

    📦 Ваш заказ № {ordercode}
    "{productname}"

    ✅ Спасибо за покупку! Если у вас будут вопросы, пишите нам на WhatsApp
    Будем благодарны, если Вы оставите отзыв о нашем магазине и товарах ⭐⭐⭐⭐⭐

    {link}

    Чтобы ссылка стала активной, напишите, пожалуйста, что-нибудь в ответ

    С уважением,
    Каспи магазин
""")
