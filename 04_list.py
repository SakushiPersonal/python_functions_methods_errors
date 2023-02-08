#Aqui recorremos un rango de numeros del 1 al 10 (el 11 no se considera) a traves de un for, para luego agregarlos con un .append a nuestra lista de numeros.
numbers = []
for number in range(1, 11):
  numbers.append(number)

print(numbers)

#Esta es una forma mucho mas limpia, simple y estilizada de hacer lo mismo que lo hecho anteriormente. directamente creamos la lista y le decimos que sera de elementos llamados "number", para luego "number" recorra el rango obteniendo asi los numeros dentro del mismo.
numbers_v2 = [number for number in range(1, 11)]

print(numbers_v2)

#Tambien le podemos agregar operativas directamente a nuestros recorridos:

numbers = []
for number in range(1, 11):
  numbers.append(number * 2)

print(numbers)

numbers_v2 = [number * 2 for number in range(1, 11)]

print(numbers_v2)

#Tambien podemos agregar condicionales para filtrar los elementos a ser contenidos en nuestra lista.
numbers = []
for number in range(1, 11):
  if number % 2 == 0:
    numbers.append(number)

print(numbers)

numbers_v2 = [number for number in range(1, 11) if number % 2 == 0]

print(numbers_v2)
