data = [43,44,64,12,78,33,11,21,58,97]

# cara 1: menghitung total data menggunakan loop for
total = 0
for i in data:
    total += i
print(total)

# cara 2: menghitung total data menggunakan method sum
print(data.sum())