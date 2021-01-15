compra1 = 356.75
compra2 = 487.45
compra3 = 295.83
compra4 = 532.00

#Fare in modo che bisogna inserire il camdio dollaro/euro
print('Introduzca el cambio $/€:')
cambio_eurdol = float(input())

#Calcolare la somma
sumacompras = (compra1 + compra2 + compra3 + compra4) * cambio_eurdol

print('La suma en euros de las compras efectuadas es:')
print(sumacompras,'€')

#Calcolare la media
mediacompras = sumacompras / 4

print('La media en euros de las compras efectuadas es:')
print(mediacompras,'€')

#Fare in modo che escano solo 2 decimali
print('Suma: {:.2f}'.format(sumacompras))
print('Media: {:.2f}'.format(mediacompras))
#Anche senza scrivere niente
print('{:.2f}'.format(sumacompras))

#Calcolare il caso in cui ci sia una diminuzione di un dato
compra4probl = compra4 * 0.8
sumacomprasprobl = (compra1 + compra2 + compra3 + compra4probl) * cambio_eurdol

print('Si en la ultima compra tenemos que pagar solo el 80% entonces la suma será:')
print(sumacomprasprobl,'€')

mediacomprasprobl = sumacomprasprobl / 4

print('Si en la ultima compra tenemos que pagar solo el 80% entonces la media será:')
print(mediacomprasprobl)

#Far vedere che tipo di dati ho stampato
print('La tipología de la información de suma en los dos casos es:')
print(type(sumacompras))
print(type(sumacomprasprobl))

#Cambiare il tipo di informazione di un dato
sumacompras1 = str(sumacompras)
sumacomprasprobl1 = str(sumacomprasprobl)

print('En versión string tendré estos dos valores:')
print(str(sumacompras))
print(str(sumacomprasprobl))