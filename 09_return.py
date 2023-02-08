#A las funciones, cuando se les indica que deben recibir uno o mas parametros, se les puede designar un valor predeterminado en caso de llamarse a la funcion sin designar parametros, asi a pesar de llamarse mal la funcion retornara aglo y no rompera el codigo. Eesto se hace poniendo un '=value' a cada parametro cuando se esta definiendo la funcion.


def find_volume(hi=10, wid=10, dep=10):
  return hi * wid * dep


result = find_volume(20, 30, 9)
print(result)

result_v2 = find_volume()
print(result_v2)

result_v3 = find_volume(dep=9)
print(result_v3)
'''''' ''''''
print('*' * 20)

#Tambien podemos decirle a la funcion que retorne mas de un valor simplemente separando con una ',' cada uno de los valores que queremos que retorne, los cuales luego seran retornados dentro de una tupla de forma predeterminada.


def find_volume(hi=10, wid=10, dep=10):
  return hi * wid * dep, wid, 'HI, this is my function'


#Podemos accededr a los distintos valores de retorno de una funcion de distintas formas:
result = find_volume(20, 30, 9)
print(result)

result_v2 = find_volume(20, 30, 9)
print(result_v2[0])

result_v3, dep, text = find_volume(20, 30, 9)
print(result_v3)
print(dep)
print(text)
