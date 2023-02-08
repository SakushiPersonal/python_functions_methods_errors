import random

dictionary = {}
for i in range(1, 11):
  dictionary[i] = i / 2

print(dictionary)

#dictionary comprehension ayuda a crear codigo mas corto, limpio y comprensible haciendo las mismas tareas que con el codigo normal, solo cque con una sintaxis mas corta.
dictionary_v2 = {i: i / 2 for i in range(1, 11)}
print(dictionary_v2)
'''''' ''''''
print('*' * 20)

countries = ['chile', 'peru', 'canada', 'suecia', 'japon']
population = {}

for country in countries:
  population[country] = str(random.randint(1, 999)) + 'M'

print(population)

#Otro ejemplo de Dictionary Comprehension:
countries = ['chile', 'peru', 'canada', 'suecia', 'japon']
population_v2 = {
  country: str(random.randint(1, 999)) + 'M'
  for country in countries
}

print(population_v2)
'''''' ''''''
print('*' * 20)

names = ['Bruno', 'Sofia', 'Emmanuel', 'Angel', 'Lisa']
ages = [25, 26, 23, 18, 19]
#para unir conjustos de listas podemos utilizar la funcion zip() :
print(list(zip(names, ages)))

#con este nuevo metodo podemos entonces crear nuestro diccionario:
personas = {name: age for (name, age) in zip(names, ages)}
print(personas)