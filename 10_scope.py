price = 100  #global


#LOCAL: una funcion local solo existe dentro de la instancia(funcion) en donde se creo y derivados, fuera de ella no existe para el codigo. Ademas al crear una variable local con el mismo nombre que una global, la funcion solo tomara la variable local y por lo tanto hay que definirla antes de hacer uso de ella.
def increment():
  price = 200  #local
  result = price + 10
  print(result)
  return result


print(price)
price_v2 = increment()
print(price_v2)
# podriamos intentar de imprimir directamente la variable 'result', la cual fue creada dentro de la funcion 'increment', pero al ser local, el codigo no la reconoce como existente fuera de la funcion, por lo cual nos daria un error en el codigo :
'''print(result)'''