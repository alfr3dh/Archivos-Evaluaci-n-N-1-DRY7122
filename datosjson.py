#importar json y datatime
import json
import datetime

#Abrir archivo JSON
with open ('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

#Obtencion de token y tiempo
token = ourjson['access_token']
t_dado = ourjson['expires_in']

#Tiempo restante antes que caduque el token (traduccion)
expira = datetime.datetime.now() + datetime.timedelta(seconds=t_dado)
restante = expira - datetime.datetime.now()


#Imprimir datos de Token y Tiempo restante
print(f"Su Token es: {token}")
print(f"Su token Expira en: {t_dado} ")
print(F"Tiempo restante antes que caduque el token : {restante}")