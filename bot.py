from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш Telegram бот.')

# Основной код
updater = Updater("5510979721:AAFPfKc8Cu8Wx8hIaaEFvqe5Lvsvqh0_vRw")

# Регистрация обработчика команды /start
updater.dispatcher.add_handler(CommandHandler("start", start))

# Запуск бота
updater.start_polling()
updater.idle()