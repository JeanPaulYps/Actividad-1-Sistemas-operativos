import os

class navegador:
    def obtenerDirectorio (self):
        return os.getcwd()
    def obtenerElementos (self):
        return os.listdir()
    def retrocederUnDirectorio(self):
        os.chdir("..")