from Model import *
from View import *
from Controller import *

#Método "principal" del módulo:
if __name__ == "__main__":
    modelo = Model1()
    vista = View_1()

    controlador = Controller(modelo, vista)

    #lógica de la aplicación en la que el controlador va a poner a 
    #interactuar al modelo y la vista
    #....