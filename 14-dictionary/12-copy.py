a = {"A": "Apel", "B":"Bengkoang", "C":"Cherry"}

print(a)
# Output: {"A": "Apel", "B":"Bengkoang", "C":"Cherry"}

b = a
c = a.copy()

b["A"] = "Anggur"
print(a)
# Output: {"A": "Anggur", "B":"Bengkoang", "C":"Cherry"}

print(c)
# Output: {"A": "Apel", "B":"Bengkoang", "C":"Cherry"}

# menugasan (assignment) pada dictionary akan diperlakukan seperti pointer
# sehingga b = a akan b pointer menunjuk ke a
# hal menyebabkan perubahan di b akan berpengaruh ke a

# berbeda dengna c = a.copy()
# perintah ini hanya menyalin data pada dictionary a ke c
# sehingga, perubahan data di c tidak akan mempengaruhi data di a