import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)
from prettytable import PrettyTable
from Nodo import Nodo
from jsonMode import showDatabases
import re

class Show(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        #Se debe llamar al metodo showDatabases() -> list:
        lista = showDatabases()
        if(len(self.hijos) < 3):
            print(lista)
            return {"Code":"0000","Message": str(len(lista)) + " rows returned", "Data" : self.mostrarData(lista)}
        else:
            reg = self.hijos[2].hijos[1].valor
            lista2 = []
            for element in lista:
                if re.search(reg.upper(),element.upper()):
                    lista2.append(element)
            return {"Code":"0000","Message": str(len(lista2)) + " rows returned", "Data" : self.mostrarData(lista2)}


    def mostrarData(self,lista):
        x = PrettyTable()

        x.field_names = ["DATABASE"]
        for item in lista:
            l = []
            l.append(item)
            x.add_row(l)
        print(x.get_string())
        return x.get_string()

    def addChild(self, node):
        self.hijos.append(node)
