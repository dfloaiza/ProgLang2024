class DataLoader:
    #atributos de clase:son comunes a todos los objetos 
    #                   de la clase}
    #atributos de instancia: son específicos de cada objeto

    #atributos de clase
    # (estáticos):
    numLoads = 0

    #atributos de instancia (son inicializados cada que se instancia
    # un nuevo objeto)
    #(en método de inicialización)
    def __init__(self, filename) -> None:
        self.filename

    def loadData(self):
        numLoads = numLoads+1


class Persona:
    #atributo de clase
    species="Homo Sapiens"
    galaxy="Vía láctea"
    average_life = "75"

    #método de inicialización (método que crea un nuevo objeto)
    #(parámetro self va en métodos de instancia)
    def __init__(self, pNombre, pEdad, pEstatura, pPeso,pIdenGenero):
        #creo atributos de "instancia"
        self.nombre = pNombre
        self.edad = pEdad
        self.estatura = pEstatura
        self.peso = pPeso
        self.genero = pIdenGenero

    # polimorfismo por sobrecarga
    # sobrecargamos la función print del objeto para que imprima los atributos:
    def __str__(self) -> str:
        if self.genero == "H":
            return f"{self.nombre} es un {self.species} de {self.edad} años que vive en la {self.galaxy}, mide {self.estatura} y pesa {self.peso}"
        else:
            return f"{self.nombre} es una {self.species} que vive en la {self.galaxy}, mide {self.estatura}"
    
#Herencia por clases abstractas
class Estudiante(Persona):

    def __init__(self, pNombre, pEdad, pEstatura, pPeso, pIdenGenero, pCarrera, pSemestre):
        super().__init__(pNombre, pEdad, pEstatura, pPeso, pIdenGenero)
        self.carrera = pCarrera
        self.semestre = pSemestre
        self.__prueba = False

    def __init__(self, pCodigo ):
        self.codigo = pCodigo

    def __init__(self, pCodigo, pNombre ):
        self.codigo = pCodigo
        self.nombre = pNombre
    
    def __str__(self) -> str:
        return super().__str__() #¿?

class Empleado(Persona):
    
    def __init__(self, pNombre, pEdad, pEstatura, pPeso, pIdenGenero,pSalario,pCargo):
        super().__init__(pNombre, pEdad, pEstatura, pPeso, pIdenGenero)
        self.salario = pSalario
        self.cargo = pCargo

    

