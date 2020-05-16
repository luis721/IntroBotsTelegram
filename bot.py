# TODA función que responde a comandos en el bot
# lleva los parámetros update y context


def start(update, context):
    update.message.reply_text("Hola mundo.")


def prueba(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido, {}.".format(nombre)
    update.message.reply_text(mensaje)

