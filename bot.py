from telegram import InlineQueryResultArticle, InputTextMessageContent, \
 InlineQueryResultVideo, ParseMode
from uuid import uuid4
import traceback

# TODA función que responde a comandos en el bot
# lleva los parámetros update y context


def start(update, context):
    update.message.reply_text("Hola mundo.")


def prueba(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido, {}.".format(nombre)
    update.message.reply_text(mensaje)


def prueba2(update, context):
	try:
		texto = update.message.text
		mensaje = "El usuario escribió {}".format(texto)
		update.message.reply_text(mensaje)
	except Exception as e:
		print(e)
		#traceback.print_stack()
		traceback.print_tb() # mostrar traceback
		#traceback.print_exception()


def imagen(update, context):
	# Obtener la ID del chat
	chat_id = update.message.chat.id
	# archivo
	img = open('./multimedia/imagen.jpg', 'rb')
	# Enviar imagen
	context.bot.send_photo(chat_id, photo=img)


def sonido(update, context):
	chat_id = update.message.chat.id
	# archivo
	snd = open("./multimedia/audio.mp3", 'rb')
	context.bot.send_audio(chat_id, audio=snd)


def inline_query(update, context):
	mensaje = "Este es un mensaje de prueba"
	# opciones a desplegar
	results = [
		InlineQueryResultArticle(
			id=uuid4(), # SE REQUIERE
			title="Prueba",
			input_message_content=InputTextMessageContent(mensaje),
			description="Test."
		),
		InlineQueryResultArticle(
			id=uuid4(), # SE REQUIERE
			title="Prueba2",
			input_message_content=InputTextMessageContent(mensaje),
			description="Test2."
		),
		# pending
		InlineQueryResultVideo(
			id=uuid4(),
			title="Recibe un video",
			video_url="https://www.youtube.com/watch?v=2HDuqHv3zos",
			mime_type="video/mp4",
			thumb_url="https://2.bp.blogspot.com/-LfB9P5GRyIY/VjETrBoHwHI/AAAAAAAAH4Q/5naYJfDbPqM/s1600/google_buscador.png"
		)
	]

	# enviar resultado
	try:
		update.inline_query.answer(results, cache_time=2)
	except Exception as e:
		traceback.print_stack()
		print(e)


# Función para el manejo de errores
def error(update, context):
    logger.warning('La solicitud "%s" causó el error "%s"', update, context.error)