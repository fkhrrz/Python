import re

choice = input("Anda akan berperan sebagai pemilik sebuah perusahaan, apakah anda siap? (ya/tidak) ")
while choice not in ["ya","tidak"]:
    print("Hanya boleh memilih \"ya\" atau \"tidak\"")
    choice = input("Anda akan berperan sebagai pemilik sebuah perusahaan, apakah anda siap? (ya/tidak) ")

if choice == "ya":
    perusahaan = input("Saya memiliki sebuah perusahaan dengan nama PT. ")
    kasir = input("Dan saya memiliki seorang kasir, namanya  ")
    sales = input("Saya juga memiliki seorang sales yang bernama ")
    dibeli = ""
    while dibeli == "":
        dibeli = input("Hari ini "+sales+" berhasil mencapai total penjualan senilai ")
        try:
            dibeli = int(dibeli)
        except ValueError:
            print("Hanya boleh menginput angka")
            dibeli = ""

    def komisi(pendapatan):
        if pendapatan > 100000:
            return str(int(pendapatan*0.30))
        elif pendapatan > 60000:
            return str(int(pendapatan*0.20))
        elif pendapatan == 60000:
            return str(int(pendapatan*0.15))

    add = ""
    for x in range(0,len(perusahaan)):
        add += "="
    print("================================================================"+add)
    print("||                            PT. "+perusahaan+"                            ||")
    print("================================================================"+add)
    print("Nama Kasir = "+kasir)
    print("Nama Sales = "+sales)
    print("Sales anda berhasil mencapai total penjualan "+str(dibeli))

    if dibeli > 100000:
        print("Sales anda mendapatkan uang jasa sebesar 50000 dan komisi sebesar "+komisi(dibeli))
    elif dibeli > 60000:
        print("Sales anda mendapatkan uang jasa sebesar 30000 dan komisi sebesar "+komisi(dibeli))
    elif dibeli == 60000:
        print("Sales anda mendapatkan uang jasa sebesar 15000 dan komisi sebesar "+komisi(dibeli))
else:
    print("Kembalilah setelah anda siap")