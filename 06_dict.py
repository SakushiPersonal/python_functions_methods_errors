import random

countries = ['chile', 'peru', 'canada', 'suecia', 'japon']

population_v2 = {
  country: str(random.randint(1, 999)) + 'M'
  for country in countries
}

print(population_v2)
'''''' ''''''
print('*' * 20)

big_countries = {
  country: population
  for (country, population) in population_v2.items()
  if int(population.replace('M', '')) > 699
}

print(big_countries)
'''''' ''''''
print('*' * 20)

text = 'Hola Lisa, soy Bruno y creo que me gustas'

unique = {
  v: (str(v.upper()) + ' ==> ' + str(text.count(v)))
  for v in text if v in 'aeiou'
}


print(unique)
