#Clase abstracta proyectil
class Projectile:
    #atributos de clase (estáticos)
    count = 0
    
    #función de instanciación o inicialización de objetos:
    def __init__ (  self, pSpeed, pDamage   ):
        self.speed = pSpeed
        self.damage = pDamage

    def shot(self):                        
        raise NotImplementedError("Implementar en clase concreta")
    
class FireProjectile(Projectile):
    def __init__(self, pSpeed, pDamage, pTime, pInt, pFireDamage):
        super().__init__(pSpeed, pDamage)
        self.time = pTime
        self.interval = pInt
        self.fireDamage = pFireDamage

    def shot(self):
        self.count += 1


class PerfProjectile(Projectile):
    def __init__(self, pSpeed, pDamage, pSurfaces):
        super().__init__(pSpeed, pDamage)
        #atributos de instancia
        self.surfaces = pSurfaces
        self.currSurfaces = 0

    def shot(self):
        self.count += 1

class ElectricProjectile(Projectile):
    def __init__(self,pSpeed, pDamage, pShockChance, pShockTime):
        super().__init__(pSpeed, pDamage)
        self.shockChance = pShockChance
        self.shockTime = pShockTime

    def shot(self):
        self.count += 1
    
    


    




