#ejercicio 18
nombres=['david','christian','dana','karen','manuel','sara', 'blanca','jose','felipe','sebastian']
def buscar_nombre(nombres):
    texto=input('ingrese nombre o parte de este a buscar\n->').lower()
    for nombre in nombres:
            if texto in nombre:
                print(f'nombre: {nombre}')
        
buscar_nombre(nombres)
