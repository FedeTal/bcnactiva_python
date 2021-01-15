cistella = {'Pomes': 3.56, 'Mandarines': 4.35, 'Síndria': 6.23, 'Maduixes': 4.28, 'Peres': 2.86, 'Taronges': 3.48}

print('Avui he comprat aquestes coses que costaven:')

print(cistella)

print('----------')

print('El preu total de la compra és:')

compratot = sum(list(cistella.values()))
print(compratot)

print('El preu mitjà de les coses que he comprat és:')

mitjana = compratot / 6
print('{:.2f}'.format(mitjana))

print('----------')

print('La llista de les primeres 4 cose que he comprat és:')

valors_cistella_reduida = list(cistella.values())[:4]
print(list(cistella.values())[:4])

print('----------')

print('He comprat llimones avui?')

print('llimones' in cistella)