import textwrap
from os import getenv
from pathlib import Path

DEBUG = 0

BOT_TOKEN = getenv("BOT_TOKEN", "define me!")

BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
DB_FILE_PATH = BASE_DIR / 'db.sqlite'
DB_URL = f'sqlite+aiosqlite:///{DB_FILE_PATH}'

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
