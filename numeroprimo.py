num1 = int(input("Ingrese el numero que quiere saber si es primo :"))

elnumeroprimo = True  #se utiliza los bulianos
if num1 < 0:
 print("Ingresa numeros postivos : ")
else:
 for i, in range(2,num1):
  if num1%i==0:
    elnumeroprimo= False

 if elnumeroprimo:
  print("el numero es primo : ")
 else:
  print("el numero no es primo : ")