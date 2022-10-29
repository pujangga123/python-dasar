# berikut adalah contoh loop  menampilkan dictionary sebagai elemen pada list
# check juga loop list-dictionary menggunakan for (file:10-perulangan-for/08-for-list-dictionary.py)

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

n = 0
while n<len(daftar):
    print("NIM :", daftar[0]['nim'])
    print("Nama :", daftar[0]['nama'])
    print("Usia :", daftar[0]['usia'])
    print("=========================")