# dictionary: daftar grade
list_grade = {
  "a" : "Sangat Baik",
  "b" : "Baik",
  "c" : "Cukup",
  "d" : "Kurang",
  "e" : "Tidak Lulus"
}

grade = input("Grade Anda (a/b/c/d/e)?")

# menampilkan elemen dari list_grade berdasarkan input user (grade)
print("Hasil :", list_grade[grade])