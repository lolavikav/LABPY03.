saldo = 1000000

def tampilkan_menu():
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
        if jumlah_tarik > saldo:
            print("Saldo tidak mencukupi!")
        else:
            saldo -= jumlah_tarik
            print("Penarikan berhasil!")
        
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1 atau 2.")