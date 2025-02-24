#ejercicio 11
import os
original_list=['manzana','uva','mora','pera','papaya','naranja']
print(f'la lista original es:{original_list}\nahora se procedera a copiarla y editarla')
copy_list=original_list.copy()
original_list.clear()
original_list=['carne','pollo','leche','atun','huevos']
print(f'las dos lista resultantes son:\nlista original={original_list}\nlista copia={copy_list}')