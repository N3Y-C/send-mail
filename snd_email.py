# Importar las librerías necesarias
import smtplib
from email.message import EmailMessage

# Crear el objeto del mensaje
msg = EmailMessage()

# Establecer el asunto, el remitente y el destinatario
msg['Subject'] = 'Hola, aqui pones tu ASUNTO'
msg['From'] = 'txxxxxxx@gmail.com' # Aquí pones tu dirección de Gmail
msg['To'] = 'jxxxxxxxx@gmail.com' # Aquí pones la dirección de Gmail a la que quieres enviar el mensaje

# Establecer el contenido del mensaje
msg.set_content('Este es el contenido del mensaje que quieres enviar por correo electrónico.')

# Crear una conexión segura con el servidor SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Aquí usas el servidor y el puerto de Gmail
    # Iniciar sesión con el usuario y la contraseña
    smtp.login('txxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx') # Aquí pones tu dirección de Gmail y la clave especial que generaste
    # Enviar el mensaje
    smtp.send_message(msg)

# Imprimir un mensaje de confirmación
print('Correo electrónico enviado con éxito.')
