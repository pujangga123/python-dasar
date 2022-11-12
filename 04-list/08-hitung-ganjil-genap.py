data = [43,44,64,12,78,33,11,21,58,97]

# cara 1: menghitung total data menggunakan loop for
ganjil = 0
genap = 0
for i in data:
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print(data)
print("Ada",genap,"bilangan genap dan",ganjil,"bilangan ganjil")
