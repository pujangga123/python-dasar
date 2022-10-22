# dictionary sebagai "database siswa"
daftar = {
    "001": {
      "nama":"Budi",
      "usia":20,
      "matkul": ["Algoritma","Struktur Data","Aljabar"]
    },
    "002": {
      "nama": "Ayu",
      "usia":22,
      "matkul": ["Algoritma", "Bahasa Inggris","Mat. Deskrit", "Mat. Logika"]
    }
}

# prompt NIM
nim = input("NIM: ")

if nim in daftar:
    print("Nama:",daftar[nim]['nama'])
    print("Usia:",daftar[nim]['usia'])
    print("Mata kuliah pertama:", daftar[nim]['matkul'][0])
    print("Jumlah Mata Kuliah:", len(daftar[nim]['matkul']) )
else:
    print("Data tidak ditemukan")