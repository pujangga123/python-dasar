# berikut adalah contoh loop  menampilkan dictionary sebagai elemen pada list
# check juga loop list-dictionary menggunakan while (file:11-perulangan-while/08-while-list-dictionary.py)

daftar = [
    {   "nim":"001",
        "nama":"Budi",
        "nilai":80
    },
    {   "nim":"002",
        "nama": "Ayu",
        "nilai":92
    },
    {   "nim":"003",
        "nama": "Yuda",
        "nilai":77
    },    
]

# variabel siswa akan berisikan elemen dictionary dari list
for siswa in daftar:
    print("NIM :", siswa['nim'])
    print("Nama :", siswa['nama'])
    print("Nilai :", siswa['nilai'])
    print("=======================")
