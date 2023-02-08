# ==> Creacion de conjunto : similar a la estructura de un dicccionario, pero sin la estructura 'clave': 'valor'
set_countries = {'chile', 'japon', 'china', 'japon'}
#Al inprimir en consola te daras cuenta que los conjuntos no permiten elementos repetidos dentro de ellos, si bien japon se encuentra considerado dos veces dentro de nuestro conjunto, al imprimirlo solo lo muestra una sola vez.
print(set_countries)
print(type(set_countries))

#Al imprimir los siguientes elementos , nos podemos dar cuenta que la impresion en cunsola no es necesariamente el el mismo orden que el escrito en codigo, esto nos demuentra que en los conjuntos no importa el orden y tampoco nos deberia importar.
set_numbers = {1, 2, 3, 69, 2000}
print(set_numbers)

set_types = {'LoveU', True, 69}
print(set_types)

#Aqui nos generara un conjunto de los caracteres que componen el string que le entregamos y mostrara cada caracter que se presente 'solo una vez', independiente de que aparezca mas de una vez.
set_from_string = set('ILoveYou')
print(set_from_string)

set_from_tuples = set(('casa', 'esposa', 'hijos', 'hijos'))
print(set_from_tuples)

#En el siguiente codigo creamos un conjunto a partir de una lista de numeros, el cual al ser impreso en consola nos mostrara cada uno de los digitos presentes, pero solo una vez (sin repetirlos).
numbers = [1, 2, 2, 2, 3, 4, 4, 69, 5, 6, 69, 7, 8, 69, 9, 0]
set_numbers = set(numbers)
print(set_numbers)

#Aqui podemos volver atomar el conjunto creado para transformarlo en una lista devuelta, pero esta vez con cada uno de los digitos presentes solo una vez.
unique_numbers = list(set_numbers)
print(unique_numbers)
