# berikut adalah contoh loop  menampilkan dictionary sebagai elemen pada list
# check juga loop list-dictionary menggunakan while (file:11-perulangan-while/08-while-list-dictionary.py)

daftar = [
    {   "nim":"001",
        "nama":"Budi",
        "usia":20
    },
    {   "nim":"002",
        "nama": "Ayu",
        "usia":22
    },
    {   "nim":"003",
        "nama": "Yuda",
        "usia":23
    },    
]

# variabel siswa akan berisikan elemen dictionary dari list
for siswa in daftar:
    print("NIM :", siswa['nim'])
    print("Nama :", siswa['nama'])
    print("Usia :", siswa['usia'])
    print("=======================")