#
from games.b import b
from games.c import c


print("""
Welcome to the ODP Games!

Silakan pilih permainan yang ingin Anda mainkan!
(1) Mencari pasangan angka dengan selisih terdekat
(2) Mengecek apakah suatu bilangan merupakan bilangan Armstrong

(0) KELUAR
""")

n = input("Pilihan Games : ")

while n != "0":
    if n == "1":
        b()
    elif n == "2":
        c()
    else:
        print('Pilihan tidak valid!')
    
    n = input("Pilihan: ")
