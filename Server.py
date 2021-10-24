import tensorflow as tf
import pandas as pd

from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

#Crear el servidor basico
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Petición GET")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Mensaje en Python desde GET".encode())

    def do_POST(self):
        print("Petición POST")
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = data.decode()
        data = parse.unquote(data)
        print(data)
        data = float(data)

        prediccion = modelo.predict([data])
        print("Predicción:", prediccion)
        
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(str(prediccion[0][0]).encode())

#Subir los datos de entrenamiento
cf = pd.read_csv("cel_a_fah.csv", sep=";")

#Crear las variables para los celcius y fahrenheits
c = cf["celcius"]
f = cf["fahrenheits"]

#Crear el modelo
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#Compilar el modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

#Entrenar la inteligencia artificial
modelo.fit(c, f, epochs=200)

#Realizar pruebas
f = modelo.predict([45])
print('Predicción:',f)

print('Iniciando el servidor')
server = HTTPServer(('localhost', 3002), servidorBasico)
server.serve_forever()