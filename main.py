import os
from dotenv import load_dotenv
import telebot
from file_reader import read_message_from_file

load_dotenv()

# Obtiene el token del bot desde las variables de entorno
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Lista de comandos disponibles
available_commands = [
    "/help", "/start", "/quienes_somos", "/mision", "/vision",
    "/valores", "/historia", "/rector", "/calidad_en_la_gestion",
    "/carreras_tecnologicas", "/identidad_corporativa"
]

# Inicializa el bot con el token proporcionado
botsito = telebot.TeleBot(TOKEN)

# Manejador de mensajes para el comando /help y /start
@botsito.message_handler(commands=["help", "start"])
def mensaje_inicial(message):
    # Mensaje inicial que se envía al usuario al iniciar o solicitar ayuda
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

    # Responde al mensaje con el mensaje inicial
    botsito.reply_to(message, initial_message)

# Manejador de mensajes para el comando /quienes_somos
@botsito.message_handler(commands=["quienes_somos"])
def mensaje_quienes_somos(message):
    # Lee el mensaje desde un archivo y lo envía como respuesta
    mensaje = read_message_from_file("quienes_somos.txt")
    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /historia
@botsito.message_handler(commands=["historia"])
def mensaje_historia(message):
    mensaje = read_message_from_file("historia.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /rector
@botsito.message_handler(commands=["rector"])
def mensaje_rector(message):
    mensaje = read_message_from_file("rector.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /calidad_en_la_gestion
@botsito.message_handler(commands=["calidad_en_la_gestion"])
def mensaje_calidad(message):
    mensaje = read_message_from_file("calidad_gestion.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /mision
@botsito.message_handler(commands=["mision"])
def mensaje_mision(message):
    mensaje = read_message_from_file("mision.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /vision
@botsito.message_handler(commands=["vision"])
def mensaje_vision(message):
    mensaje = read_message_from_file("vision.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /valores
@botsito.message_handler(commands=["valores"])
def mensaje_valores(message):
    mensaje = read_message_from_file("valores.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /carreras_tecnologicas
@botsito.message_handler(commands=["carreras_tecnologicas"])
def mensaje_valores(message):
    mensaje = read_message_from_file("carreras.txt")

    botsito.reply_to(message, mensaje)

# Manejador de mensajes para el comando /identidad_corporativa
@botsito.message_handler(commands=["identidad_corporativa"])
def identidad_corporativa(message):
    # Envía un mensaje con los colores corporativos
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

    # Envía un grupo de medios que contienen imágenes con subtítulos
    image_paths = ["images/logo-full-itla-preview.jpg", "images/logo-fondo-blanco-preview-1.jpg", "images/logo-fondo-azul-preview-1.jpg"]
    media = []
    for index, path in enumerate(image_paths):
        with open(path, 'rb') as img:
            media.append(telebot.types.InputMediaPhoto(img.read(), caption=f"Logo ITLA {index + 1}"))

    botsito.send_media_group(message.chat.id, media)

# Manejador de mensajes para completar comandos
@botsito.message_handler(func=lambda message: True)
def autocomplete_commands(message):
    # Convierte el texto del mensaje en minúsculas
    text = message.text.lower()

    # Encuentra comandos sugeridos que coincidan con el texto del mensaje
    suggested_commands = [cmd for cmd in available_commands if cmd.startswith(text)]

    # Si hay comandos sugeridos, responde con ellos
    if suggested_commands:
        reply = "Quisiste decir: " + "\n".join(suggested_commands)
        botsito.reply_to(message, reply)
    # Si no hay comandos sugeridos, responde con un mensaje predeterminado
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

# Inicia el bot para escuchar mensajes entrantes
if __name__ == "__main__":
    botsito.polling(none_stop=True)
