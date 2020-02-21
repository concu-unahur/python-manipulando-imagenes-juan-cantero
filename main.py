from concatenacion import *
from archivos import *
from api import PixabayAPI
import logging

  

api = PixabayAPI('15310730-4b58aad1f4a3657eafdaf8dd6', carpeta_imagenes)
query = "perros"
logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 5)






#for u in urls:
#   api.descargar_imagen(u)


lista = []
for u in urls:
    api.descargar_imagen(u)
    api.guardarImagenesEnLista(u,lista)

imagenes = []

for path in lista:
    imagenes.append(leer_imagen(path))

print(lista[0])    

print(len(imagenes))


for i in range(len(imagenes)):
    escribir_imagen(f'concatenada-vertical{i}.jpg', concatenar_vertical([imagenes[i], imagenes[i+1]]))    




