import os
from dotenv import load_dotenv
import telebot
from file_reader import read_message_from_file

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

available_commands = [
    "/help", "/start", "/quienes_somos", "/mision", "/vision",
    "/valores", "/historia", "/rector", "/calidad_en_la_gestion",
    "/carreras_tecnologicas", "/identidad_corporativa"
]

botsito = telebot.TeleBot(TOKEN)
@botsito.message_handler(commands=["help", "start"])

def mensaje_inicial(message):
    initial_message = "¡Hola! ¿Cómo estás?\n \n"
    initial_message += "Este bot es para consultar información sobre el Instituto Tecnológico de las Américas (ITLA) \n \n"
    initial_message += "Estos son algunos comandos que puedes ejecutar: \n"
    initial_message += "/quienes_somos - Conocer quiénes somos. \n"
    initial_message += "/mision - Conocer nuestra misión. \n"
    initial_message += "/vision - Conocer nuestra visión. \n"
    initial_message += "/valores - Conocer nuestros valores. \n"
    initial_message += "/historia - Conocer nuestra historia. \n"
    initial_message += "/rector - Conoce a nuestro rector. \n"
    initial_message += "/identidad_corporativa - Colores y logos corporativos. \n"
    initial_message += "/calidad_en_la_gestion - Calidad en la Gestión. \n"
    initial_message += "/carreras_tecnologicas - Conoce nuestras carreras tecnológicas. \n"

    botsito.reply_to(message, initial_message)

@botsito.message_handler(commands=["quienes_somos"])

def mensaje_quienes_somos(message):
    mensaje = read_message_from_file("quienes_somos.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["historia"])
def mensaje_historia(message):
    mensaje = read_message_from_file("historia.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["rector"])
def mensaje_rector(message):
    mensaje = read_message_from_file("rector.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["calidad_en_la_gestion"])
def mensaje_calidad(message):
    mensaje = read_message_from_file("calidad_gestion.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["mision"])
def mensaje_mision(message):
    mensaje = read_message_from_file("mision.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["vision"])
def mensaje_vision(message):
    mensaje = read_message_from_file("vision.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["valores"])
def mensaje_valores(message):
    mensaje = read_message_from_file("valores.txt")

    botsito.reply_to(message, mensaje)

@botsito.message_handler(commands=["carreras_tecnologicas"])
def mensaje_valores(message):
    mensaje = read_message_from_file("carreras.txt")

    botsito.reply_to(message, mensaje)


@botsito.message_handler(commands=["identidad_corporativa"])
def identidad_corporativa(message):
    colores = "Colores Corporativos: \n"
    colores += """
#023877
2R 56G 119B
100C 87M 27Y 12K

#E52229
229R 34G 41B
4C 99M 95Y 0K
"""
    botsito.send_message(message.chat.id, colores)

    image_paths = ["images/logo-full-itla-preview.jpg", "images/logo-fondo-blanco-preview-1.jpg", "images/logo-fondo-azul-preview-1.jpg"]

    media = []
    for index, path in enumerate(image_paths):
        with open(path, 'rb') as img:
            media.append(telebot.types.InputMediaPhoto(img.read(), caption=f"Logo ITLA {index + 1}"))

    botsito.send_media_group(message.chat.id, media)

@botsito.message_handler(func=lambda message: True)
def autocomplete_commands(message):
    text = message.text.lower()

    suggested_commands = [cmd for cmd in available_commands if cmd.startswith(text)]

    if suggested_commands:
        reply = "Quisiste decir: \n" + "\n".join(suggested_commands)
        botsito.reply_to(message, reply)
    else:
        default_message = """
Ejecuta uno de estos comandos:

/quienes_somos - Conocer quiénes somos. 
/mision - Conocer nuestra misión. 
/vision - Conocer nuestra visión. 
/valores - Conocer nuestros valores. 
/historia - Conocer nuestra historia. 
/rector - Conoce a nuestro rector. 
/identidad_corporativa - Colores y logos corporativos. 
/calidad_en_la_gestion - Calidad en la Gestión. 
/carreras_tecnologicas - Conoce nuestras carreras tecnológicas.
        """
        botsito.reply_to(message, default_message)

if __name__ == "__main__":
    botsito.polling(none_stop=True)

