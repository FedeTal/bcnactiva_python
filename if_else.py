eta_persone = {'Fede': 34, 'Bea': 37, 'Lucia': 65, 'Stefano': 64}
print('Questa è la lista delle persone:')
print(eta_persone)
print('Introduci il tuo nome per aggiungerti alla lista:')
nome_persona = input()

if nome_persona in eta_persone:
    print('Nome già presente nella lista!')
else:
    print('Inserisci la tua eta:')
    eta_nuova_persona = int(input())
    eta_persone[nome_persona] = eta_nuova_persona
    print('Sei stato aggiunto alla lista!')
    print('La lista delle persone aggiornata:')
    print(eta_persone)




