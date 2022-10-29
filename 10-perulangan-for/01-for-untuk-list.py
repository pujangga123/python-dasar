listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

print('Tanpa penomoran:')

for kota in listKota:
  print(kota)

print('\nDengan penomoran (enumerate):')

for i, kota in enumerate(listKota):
  print(i, kota)