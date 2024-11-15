from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я ваш Telegram бот.')

# Основной код
app = Application.builder().token("").build()

# Регистрация обработчика команды /start
app.add_handler(CommandHandler("start", start))

# Запуск бота
app.run_polling()