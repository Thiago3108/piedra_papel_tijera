print("-------------------------------")
print("-----PIEDRA, PAPEL O TIJERA----")
print("-------------------------------")

print("1 ==> Piedra")
print("2 ==> Papel")
print("3 ==> Tijera")
#input
import random

bandera = False

user = int(input("Seleccione opcion: "))
computer = random.randint(1,3)
piedra= 1
papel=2
tijera=3
# procesing           
if user == 1:
    if computer==2:
        rta="PERDISTE"
    elif computer==3:
        rta="GANASTE"
    else:
        rta="EMPATE"
elif user == 2:
    if computer==1:
        rta="GANASTE"
    elif computer==2:
        rta="EMPATE"
    else:
        rta="PERDISTE"
elif user==3:
    if computer==2:
        rta="GANASTE"
    elif computer==3:
        rta="EMPATE"
    else:
        rta="PERDISTE"
else:
    bandera=True
# option user
if user==1:
    rta2="Piedra"
elif user ==2:
    rta2="Papel"
elif user ==3:
    rta2="Tijera"
# option computer
if computer==1:
    rta3="Piedra"
elif computer ==2:
    rta3="Papel"
elif computer ==3:
    rta3="Tijera"
#output
if bandera==False:
   h="*"*10
   print(h)
   print(rta)
   print(h)
   print("opcion del user ==> ", str(rta2))
   print("Opcion del computer ==> ", str(rta3))
   print(h)
else:
    h="*"*10
    bandera==True
    print(h)
    print("Elegiste perder!!!")
    print(h)
    


    
