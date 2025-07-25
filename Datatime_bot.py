import os
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загрузка переменной окружения из .env
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я простой бот.\n\n Доступные команды:\n\n1. /time \n2. /date")

# Команда "/time": возвращает текущее время
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now().strftime('%H:%M:%S')
    await update.message.reply_text(f"Текущее время: {current_time}")

# Команда "/date": возвращает текущую дату
async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_date = datetime.now().strftime('%d-%m-%Y')
    await update.message.reply_text(f"Сегодняшняя дата: {current_date}")

# Основная точка входа программы
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчик команды /start
    app.add_handler(CommandHandler('start', start))

    # Регистрация обработчиков команд
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("date", date_command))

    # Запуск бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()