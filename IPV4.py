#Preguntar por su IPv4
ip = int(input("Por favor, introduzca el número de ACL IPv4 \n"))

#saber si es estandar, extendida o el número no corresponde y mostrar print

#Saber si es estandar entre el ranfo de 1 a 99
if ip >= 1 and ip <=99:
    print("El numero corresponde a una ACL Estándar")

#Saber si es Extedida entre el rango 100 a 199
elif ip >= 100 and ip <=199:
    print("El numero corresponde a una ACL Extendida")

#Si no esta entre 1 a 199, el número no corresponde a una lista de acceso.
else:
    print("El número no corresponde a una lista de acceso.")