#En el siguiente print nos mostrara la cantidad de elementos que posee nuestro conjunto, y como podras ver luego, no considera elementos repetidos, por lo cual nuestra la cantidad ded elementos UNICOS dentro del conjunto.
set_countries = {'chile', 'japon', 'china', 'japon'}
size = len(set_countries)
print(size)

print('chile' in set_countries)
print('peru' in set_countries)

#agregar un elementos al conjunto a traves de .add . como se puede ver aun si le agragamos mas de una vez el mismo elemento, al imprimirlo, no lo repetira.
set_countries.add('peru')
print(set_countries)
set_countries.add('peru')
print(set_countries)

#con .update podemos agregarle un conjunto de elementos a nuestro conjunto, y a su vez seguira respetando las reglas de los conjuntos (-no repite elementos, -no posee orden).
set_countries.update({'argentina', 'estados unidos', 'peru'})
print(set_countries)

#remove
set_countries.remove('argentina')
print(set_countries)

#set_countries.remove('canada') ==> al intentar de remover un elemento que no existe con el metodo .remove, python lanzara un error directamente, por lo cual nos detendra el codigo.


#Para evitar que se nos rompa el codigo al intentar de eliminar un elemento de un conjunto, podemos utilizar el metodo .discard, con el cual de no existir el elemento que queremos eliminar, simplemente no hara nada.
set_countries.discard('canada')
print(set_countries)

#Con el metodo .clear, eliminaremos todos los elementos contenidos en nuestro conjunto, quedando asi completamente vacio.
set_countries.clear()
print(set_countries)
print(len(set_countries))