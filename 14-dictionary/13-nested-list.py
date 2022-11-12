# contoh penggunaan dictionary (dalam list)
daftar = [
    { "nama": "Budi", "jk": "L", "usia" : 32 },
    { "nama": "Ayu Diah", "jk": "P", "usia": 22 },
    { "nama": "Yuda Chandra", "jk": "L", "usia": 43},
    { "nama": "Nina Yosephin", "jk": "P", "usia": 24},
    { "nama": "Gilang", "jk":"L", "usia": 21}
]
# catatan:
# jk = jenis kelamin

# loop menampilkan data dictionary dalam list
n = 1
for peserta in daftar:
    print(n, peserta['nama'], peserta['jk'], peserta['usia'])
    n += 1