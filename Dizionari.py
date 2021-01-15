#I dizionari sono formati da una lista di voci
# con coppie di keys e values
eta_persone = {'Fede': 34, 'Bea': 37, 'Lucia': 65, 'Stefano': 64}

#Per stampare il dizionario
print(eta_persone)

#Posso ricavare il valore di una key attraverso 2 metodi
anni_bea = eta_persone['Bea']
anni_bea = eta_persone.get('Bea')

#In ogni caso per stamparlo non ho bisogno di creare una variabile nuova
print(eta_persone['Bea'])
print(anni_bea)
print(eta_persone.get('Bea'))


#Per aggiungere una nuova voce
eta_persone['Pietro'] = 3

print(eta_persone)

# Per togliere una voce
del eta_persone['Pietro']

print(eta_persone)


#Per saper quante voci ci sono nel dizionario
print(len(eta_persone))


#Per creare una lista delle sole keys o delle sole values
persone = eta_persone.keys()
lista_persone = list(persone)

print(lista_persone)

anni = eta_persone.values()
lista_anni = list(anni)

print(lista_anni)

#Posso creare le liste direttamente senza creare variabili intermedie
# Creando il nome della lista
lista_persone1 = list(eta_persone.keys())
lista_anni1 = list(eta_persone.values())
print(lista_persone1)
print(lista_anni1)
# Creando il nome dell'insieme dei dati
persone = eta_persone.keys()
anni = eta_persone.values()
print(list(persone))
print(list(anni))

#Per sapere se una key o un values sono in un dizionario/lista faremo cosí:
print('Cicciobombo' in lista_persone)
print(34 in lista_anni)
print('Fede' in eta_persone)     # Se cerchiamo direttamente nel dizionario ci dice solo se è una key!!
print(34 in eta_persone)        # Infatti qui verrà fuori False anche se è presente come value!!
# Il valore che ci verrà dato è booleano (True/False)


# Per creare una lista con le voci del dizionario
personeanni = eta_persone.items()
lista_personeanni = list(personeanni)
#oppure direttamente
lista_personeanni = list(eta_persone.items())

print(lista_personeanni)
print(lista_personeanni)


# Le liste (e i dizionari stessi) possono essere parte di un dizionario
dizionario1 = {'a': 24,'b': 9.5,'c': True, 'Seriez': [3,1,7],
               'Dizzy': {'blu': 1, 'giallo':2}}

print(dizionario1)


# Se vogliamo prendere una posizione concreta della serie dentro il dizionario:
ilnumerochevoglio = dizionario1['Seriez'][2]

print(dizionario1['Seriez'][2])
print(ilnumerochevoglio)

# Possiamo prendere anche il value di una determinata key di un sotto-dizionario
print(dizionario1['Dizzy']['blu'])





