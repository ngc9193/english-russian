pip install python-telegram-bot

from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator

def translate_message(update, context):
    message = update.message.text
    translator = Translator()
    translated_message = translator.translate(message, src='en', dest='ru').text
    update.message.reply_text(translated_message)

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

