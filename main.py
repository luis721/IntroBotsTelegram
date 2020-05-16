from config import TOKEN
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
#from telegram import 
import bot
# @mi_primer_bot_ist_bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # COMANDOS

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("prueba", bot.prueba))
    dispatcher.add_handler(CommandHandler("prueba2", bot.prueba2))
    dispatcher.add_handler(CommandHandler("imagen", bot.imagen))
    dispatcher.add_handler(CommandHandler("sonido", bot.sonido))
    # inline queries 
    """
    Para poder permitir las inline queries en el bot
    es necesario activarlas primero en Bot Father.
    """
    dispatcher.add_handler(InlineQueryHandler(bot.inline_query))
    # Para el manejo de errores
    dispatcher.add_error_handler(bot.error)
    # INICIAR EL BOT
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
