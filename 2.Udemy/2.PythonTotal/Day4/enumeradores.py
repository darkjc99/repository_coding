#lista = ['a','b','c']
#for indice,item in enumerate(lista):
#    print(indice,item)

#for indice,item in enumerate(range(50,55)):
#    print(indice,item)

#lista = ['a','b','c']
#mis_tuples= list(enumerate(lista))
#print(mis_tuples[1][1])


#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#tuple=list(enumerate(lista_nombres))
#for i in tuple:
#    print(f'{i[1]} se encuentra en el índice {i[0]}')

#texto = 'Python'
#letras = list(texto)
#lista_indices = list(enumerate(letras))
#print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
tuple=list(enumerate(lista_nombres))
for i in tuple:
    if i[1][0:1] == 'M':
        print(f'{i[0]}')