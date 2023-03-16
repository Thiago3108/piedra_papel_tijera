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
p = "piedra"
pa= "papel"
t="tijera"
# procesing           
if user == 1:
    option=p
    if computer==2:
        optionC=pa
        rta="PERDISTE"
    elif computer==3:
        optionC=t
        rta="GANASTE"
    else:
        optionC=p
        rta="EMPATE"
elif user == 2:
    option=pa
    if computer==1:
        optionC=p
        rta="GANASTE"
    elif computer==2:
        optionC=pa
        rta="EMPATE"
    else:
        optionC=t
        rta="PERDISTE"
elif user==3:
    option=t
    if computer==2:
        optionC=pa
        rta="GANASTE"
    elif computer==3:
        optionC=t
        rta="EMPATE"
    else:
        optionC=p
        rta="PERDISTE"
else:
    bandera=True
#output
if bandera==False:
   print(rta)
   print("opcion del user ==> ", str(option))
   print("Opcion del computer ==> ", str(optionC))
else:
    bandera==True
    print("Elegiste perder!!!")
    


    
