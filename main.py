from config import TOKEN
from telegram.ext import Updater, CommandHandler
from bot import start, prueba
# @mi_primer_bot_ist_bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("prueba", prueba))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
