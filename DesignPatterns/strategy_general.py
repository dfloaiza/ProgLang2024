class GeneralImpl:
    def execute():
        pass

class SpecificImplA(GeneralImpl):
    def execute(self):
        print ("A través de implementación A")

class SpecificImplB(GeneralImpl):
    def execute(self):
        print("A través de implementación B")

class Context:
    def __init__(self,impl:GeneralImpl):
        self.impl = impl

    def execute_impl(self):
        self.impl.execute()

ImplA = SpecificImplA()
contexto_impl1 = Context(SpecificImplA)
result_impl1 = contexto_impl1.execute_impl()

ImplB = SpecificImplB()
contexto_impl2 = Context(SpecificImplB)
result_impl2 = contexto_impl2.execute_impl()

