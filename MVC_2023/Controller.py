from Model import *
from View import *

class Controller:

    #recibe como parámetros el modelo y la vista que está actualizando:
    def __init__(this, model, view):
        this.model = model
        this.view = view

    def updateView(self):
        pass

    def updateModel(self):
        pass