import telegram
bot = telegram.Bot(token='5805987840:AAE6BpOqEhoy9QjkM0pkjP1JTd1yqjYwHUQ') 
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
updater = Updater(token='5805987840:AAE6BpOqEhoy9QjkM0pkjP1JTd1yqjYwHUQ', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()
