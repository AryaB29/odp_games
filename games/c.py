
def c():
        n = int(input("Masukan Nilai Awalnya : "))
        if True:
            nilai = [int(digit) for digit in str(n)]
            hasil = []
            nilai_awal = 1
            for i in nilai:
                nilai_awal = nilai_awal * (i**3)
                hasil.append(nilai_awal)
                nilai_awal = 1

            if sum(hasil) == n:
                print("Bilangan Armstrong")
            else:
                print("Bukan Bilangan Armstrong")
        else:
            print("Masukan Bilangan Numerik")
