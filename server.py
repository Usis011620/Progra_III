from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector 
import json

class crud:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root',
                                                port='3302', 
                                                password='',
                                                host='localhost', 
                                                database='db_sistemaclinica')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')
crud = crud()

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/insertar':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = data.decode('utf-8')
            data = parse.unquote(data)
            data = json.loads(data)

print('Servidor iniciado en el puerto 3000')
servidor = HTTPServer(('localhost', 3000), servidorBasico)
servidor.serve_forever()