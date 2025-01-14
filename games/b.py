#
def is_valid_list(data):
    differences = list(map(lambda x, y: abs(x - y), data[:-1], data[1:]))
    return len(differences) == len(set(differences))

def b():
    user_input = input("Masukkan elemen list, dipisahkan dengan koma: ")
    data = [int(item.strip()) for item in user_input.split(",")]
    list_kosong = [abs(data[0] - data[1])]
    if is_valid_list(data):
        for i in data:
            for j in list(range(1,len(data))):
                if i != data[j]:
                    if abs(i - data[j]) < list_kosong[0]:
                        hasil = [i,data[j]]
                else:
                    pass
        print(hasil)
    else:
        print("Selisih angka harus berbeda")
