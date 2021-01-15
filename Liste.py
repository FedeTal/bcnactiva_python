#Le liste possono essere di dati dello stesso tipo o di diverso tipo:
lista1 = [7,'ciao',9.4,True]
lista2 = [3,6,2,7,1]

print(lista1)
print(lista2)


#Posso riferirmi a una posizione concreta della lista
#Partendo da 0 quando conto da sinistra
#Partendo da -1 quando conto da destra
a = lista1 [0]
a = lista1 [-4]

b = lista2 [4]
b = lista2 [-1]

#Posso direttamente stampare la posizione senza creare la variabile
print(lista1[0])
print(lista1[-4])


#Posso calcolare la lunghezza della lista (come anche quella di una parola)
lunghezza_lista = len(lista1)
lunghezza_parola = len('Federico')

print(lunghezza_lista)
print(len('Federico'))

#Possiamo aggiungere un dato alla lista (Automaticamente si aggiungerà come ultimo)
lista1.append('Caccola')
print(lista1)

#Possiamo togliere un dato della lista (si può scegliere quale togliere???)
#Se non specifichiamo quale dato togliere toglierà automaticamente l'ultimo
lista1.pop()   #sarà lo stesso che scrivere lista1.pop('Caccola')

print(lista1)


#Per sapere quale posizione occupa un dato:
posizione_ciao = lista1.index('ciao')
print(lista1.index('ciao'))


#Per selezionare solo alcuni dati della lista:
lista3 = lista1[1:3]    #Non si considera il dato alla posizione dell'indice a destra (in questo caso 3)

lista4 = lista2[1:]   #Dalla posiz 1 in poi
lista5 = lista2[:3]   #Dalla posiz 0 fino alla 2 (la 3 non si considera)
lista6 = lista2[:2] + lista2[3:]

#Posso creare la nuova variabile lista6 o mettere tutto direttamente in print
print(lista6)
print(lista2[:2] + lista2[3:])
#Se lo metto con la virgola mi verrano due listine staccate
print(lista2[:2],lista2[3:])