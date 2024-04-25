from Module1_2024 import *

myFireProj = FireProjectile(35,60,10,0.2,1.5)
myElectricProj = ElectricProjectile(120,20,0.7,3)
myPerfProj = PerfProjectile(15,24,4)

print(isinstance(myElectricProj,Projectile))
print(isinstance(myPerfProj,Projectile))
print(isinstance(myFireProj,Projectile))


myFireProj.shot()
myPerfProj.shot()
myElectricProj.shot()

print(myElectricProj.count)