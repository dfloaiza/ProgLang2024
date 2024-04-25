#### Patrón Estructural Adapter
#clase *adaptada con interfaz no compatible con el *cliente a través de un *adaptador
class Server:
    def __init__(self):
        pass

    def request_trans(self):
        return "Petición adaptada a la interfaz del cliente"

#clase cliente
class Client:
    def __init__(self):
        pass

    def request(self):
        return "Petición del cliente"


class ImplPattern(Client):
    def __init__(self, srv:Server):
        self.srv = srv

    def request(self):
        return self.srv.request_trans()
  
class Implementation:
    def execute():
        pass

#estrategias concretas:
class ConcreteImplA(Implementation):
    def execute(self):
        print ("Ejecutando estrategia concreta A")

class ConcreteImplB(Implementation):
    def execute(self):
        print("Ejecutando estrategia concreta B")

#la clase Context es la que le permite al cliente ejecutar la estrategia correspondiente:
class Context:
    def __init__(self,strategy:Implementation):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

#ejemplo de uso del patrón strategy (general):
#usando la estrategia A
strategyA = ConcreteImplA()
contexto_str1 = Context(strategyA)
result_str1 = contexto_str1.execute_strategy()

#usando la estrategia B
strategyB = ConcreteImplB()
contexto_str2 = Context(strategyB)
result_str2 = contexto_str2.execute_strategy()






