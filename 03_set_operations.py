set_a = {'chile', 'peru', 'canada'}
set_b = {'argentina', 'estados unidos', 'chile'}

#UNION: en las siguientes operaciones estamos uniendo dos conjuntos para crear uno nuevo con el contenido de ambos (no repite elementos), una de ellas es atraves de un metodo, y  la otra opcion es atraves de un operador directamente.
set_c = set_a.union(set_b)
print(set_c)

print(set_a | set_b)

#INTERSECCION: en estas operaciones estaremos buscando como resultado los elementos que esten en ambos conjuntos a la vez. Una vez mas a traves de un metodo y a traves de un operador.
set_c = set_a.intersection(set_b)
print(set_c)

print(set_a & set_b)

#DIFERENCIAS: aqui intentamos de quitarle al primer conjunto (set_a) los elementos del segundo conjunto (set_b), lo cual nos estaria dando el restante en conjuntoA - conjuntoB.
set_c = set_a.difference(set_b)
print(set_c)

print(set_a - set_b)

#DIFERENCIA SIMETRICA: en esta operacion estamos buscando los elementos que son distintos entre dos conjuntos y esos entregarlos como resultado en un nuevo conjunto.
set_c = set_a.symmetric_difference(set_b)
print(set_c)

print(set_a ^ set_b)