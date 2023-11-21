import pathlib
import pymysql
import os
import pandas as pd
import smtplib
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText


def getData():
  print('FUNCTION GET DATA')
  
  
  path = pathlib.Path(__file__).parent.absolute()
  print(path)
  
  contenido = os.listdir()
  print(contenido)


  for file in contenido:
    print(file)
    if file == 'params.txt.txt':
      params_path = str(path)+'\\' +file
      
      with open(params_path, 'r') as archivo:
          contenido = archivo.read()
      date_param = contenido

  print(date_param)
  
  
  endpoint = 'diri.cacwiynywmfv.us-east-2.rds.amazonaws.com'
  username = 'lsanchez' 
  password = 'Mely_2011!'
  database_name = 'diriprod'
  
  connection = pymysql.connect(host=endpoint,
                                 user=username,
                                 password=password,
                                 database=database_name,
                                 cursorclass=pymysql.cursors.DictCursor)
  cursor = connection.cursor()
  
  if date_param:
    sql = f"select id, folio, nombre_linea, referencia from diri_preventa where fechafinal < '{date_param}' limit 10"
  else:
    return ('ERROR EN EL PARAMETRO DE FECHA')
  print(sql)
  cursor.execute(sql)
  data = cursor.fetchall()
  
  
  print(data)
  
  df = pd.DataFrame(data)

  # Crear un archivo Excel
  archivo_excel = "datos.xlsx"
  df.to_excel(archivo_excel, index=False)

  print(f"Archivo Excel '{archivo_excel}' creado satisfactoriamente.")
  
  # Crea la conexión SMTP
  server = smtplib.SMTP('smtp.gmail.com', 587)

  correo = 'jeduarte@diri.mx'
  pas ='Hellandheaven1'
  # Inicia sesión en tu cuenta de Gmail
  server.starttls()

  server.login(correo, pas)

  # Definir el remitente y destinatario del correo electrónico
  remitente = "jeduarte@diri.mx"
  destinatario = "yflores@diri.mx"
  
  # Crear el mensaje del correo electrónico
  mensaje = email.mime.multipart.MIMEMultipart()
  mensaje['From'] = remitente
  mensaje['To'] = destinatario
  mensaje['Subject'] = "Correo electrónico con archivo adjunto"

  # Añadir el cuerpo del mensaje
  cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n :)"
  mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

  # Añadir el archivo Excel como adjunto
  ruta_archivo = str(path) + '/datos.xlsx'
  archivo = open(ruta_archivo, 'rb')
  adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
  adjunto.set_payload((archivo).read())
  email.encoders.encode_base64(adjunto)
  adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
  mensaje.attach(adjunto)

  # Convertir el mensaje a texto plano
  texto = mensaje.as_string()

  # Enviar el correo electrónico
  server.sendmail(remitente, destinatario, texto)

  # Cerrar la conexión SMTP
  server.quit()





print(pathlib.Path(__file__).parent.absolute())
# print(contenido)
print(getData())
# print(create_report())