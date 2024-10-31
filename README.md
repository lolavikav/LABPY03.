# LABPY03.

# Nama : Lola Seftyliani
# Kelas : TI.24.A.4
# NIM : 312410339

## Soal Latihan

![TUGASSSSSS](https://github.com/user-attachments/assets/5ddcf801-cc0c-422c-acf7-5a489cd9c2cc)

## Latihan1.py

```python
from random import random
n = int(input("Masukkan nilai N: "))

for i in range(1, n + 1):
    angka_acak = random()
    if angka_acak < 0.5:
        print(f"data ke: {i} => {angka_acak}")
    else:
        while angka_acak >= 0.5:
            angka_acak = random()
        print(f"data ke: {i} => {angka_acak}")

print("Selesai")
```

```python
from random import random
```

Baris ini mengimpor modul random, yang berisi fungsi-fungsi untuk menghasilkan angka acak.

```python
n = int(input("Masukkan nilai N: "))
```

Pengguna meminta untuk memasukkan nilai integer n yang menentukan berapa banyak angka acak yang akan dihasilkan. Fungsi input() menerima masukan dari pengguna dalam bentuk string, dan int() mengonversinya menjadi integer.

```python
for i in range(1, n + 1):
```

for adalah perulangan yang akan berjalan sebanyak N kali, range(1, n + 1) menghasilkan urutan angka mulai dari 1 hingga N (termasuk N), yang digunakan untuk menentukan jumlah angka acak yang akan dihasilkan.

```python
angka_acak = random()
        print(f"data ke: {i} => {angka_acak}")
```

Di dalam perulangan, random.random() digunakan untuk menghasilkan angka acak dalam rentang 0.0 hingga 1.0, dengan nomor urut datanya (data ke: {i}). Format {i} dan {angka_acak} digunakan dalam f-string untuk menampilkan nilai variabel i dan angka_acak secara langsung di dalam string.

```python
print("Selesai")
```

Setelah perulangan selesai, baris ini menampilkan pesan "Selesai" untuk menandakan bahwa program telah selesai menjalankan seluruh instruksi.

## Code program tersebut

![Screenshot 2024-10-30 164016](https://github.com/user-attachments/assets/555c005f-672e-4124-97d1-27c46df11fdf)

## Hasil dari program tersebut

![Screenshot 2024-10-30 164137](https://github.com/user-attachments/assets/ecea8e69-c298-4c75-a5f6-f63e788d6939)

# Latihan2.py
# Menghitung Laba Usaha selama 8 Bulan

## Deskripsi 

Program ini melakukan perhitungan laba bulanan dengan aturan sebagai berikut:
1. **Bulan 1 dan 2**: Belum mendapatkan laba (0%).
2. **Bulan 3 dan 4**: Mendapatkan laba sebesar 1% dari modal awal.
3. **Bulan 5, 6, dan 7**: Mendapatkan laba sebesar 5% dari modal awal.
4. **Bulan 8**: Mengalami penurunan laba menjadi 3% dari modal awal.

Program akan menghitung laba untuk setiap bulan dan menampilkan hasilnya. Setelah 8 bulan, program juga menampilkan total laba yang diakumulasi selama periode tersebut.

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan program ini sebagai latihan2.py.
3. Buka terminal atau command prompt di lokasi penyimpanan file tersebut.
4. Jalankan perintah berikut:

```python
python3 latihan2.py
```

## Penjelasan Kode

## 1. Modal Awal dan Variabel Laba

```python
modal_awal = 100_000_000
total_laba = 0
```

```python
modal_awal: menyimpan modal awal pengusaha, yaitu 100 juta rupiah.
total_laba: akumulasi total laba dari bulan 1 hingga 8, dimulai dari 0.
```

## 2. Lingkaran Perhitungan Laba per Bulan

```python
for bulan in range(1, 9):
    if bulan in [1, 2]:        # Bulan 1 dan 2 belum mendapatkan laba
        laba = 0
    elif bulan == 3:           # Bulan 3 mendapatkan laba 1%
        laba = 0.01 * modal_awal
    elif bulan == 4:           # Bulan 4 mendapatkan laba 1%
        laba = 0.01 * modal_awal
    elif bulan == 5:           # Bulan 5 mendapatkan laba 5%
        laba = 0.05 * modal_awal
    elif bulan in [6, 7]:      # Bulan 6 dan 7 mendapatkan laba 5%
        laba = 0.05 * modal_awal
    elif bulan == 8:           # Bulan 8 mendapatkan laba 3%
        laba = 0.03 * modal_awal
```

- Bulan 1 dan 2 : laba 0%.
- Bulan 3 dan 4 : laba 1% dari modal awal.
- Bulan 5, 6, dan 7 : laba 5% dari modal awal.
- Bulan 8 : laba 3% dari modal awal.

## 3. Menambahkan Laba ke Total Laba dan Menampilkan Laba per Bulan

``` python
total_laba += laba
print(f"laba bulan ke- {bulan} sebesar: {laba}")
```

## 4. Akhir Program: Menampilkan Total Laba

Setelah loop selesai, program menampilkan total laba yang diperoleh selama 8 bulan.

## Contoh Output

Jika Anda menjalankan program ini, outputnya mungkin akan terlihat seperti berikut

```python
laba bulan ke- 1 sebesar: 0
laba bulan ke- 2 sebesar: 0
laba bulan ke- 3 sebesar: 1000000.0
laba bulan ke- 4 sebesar: 1000000.0
laba bulan ke- 5 sebesar: 5000000.0
laba bulan ke- 6 sebesar: 5000000.0
laba bulan ke- 7 sebesar: 5000000.0
laba bulan ke- 8 sebesar: 3000000.0
Total laba adalah: 19000000.0
```

## Berikut adalah hasin screenshot vsc
-


## LATIHAN 3.latihan3.py 

## Simulasi Mesin ATM Sederhana

## Deskripsi

Program ini adalah simulasi mesin ATM sederhana yang memungkinkan pengguna untuk melakukan penarikan uang dengan saldo awal sebesar Rp 1.000.000. Pengguna dapat memilih untuk menarik uang atau keluar dari sistem.

## Fitur Program

1.Menampilkan Saldo - Program akan selalu menampilkan saldo saat ini.
2.Penarikan Uang - Pengguna dapat melakukan penarikan uang dengan nominal tertentu.
3.Validasi Saldo - Program akan mengecek apakah saldo mencukupi sebelum memproses penarikan.
4.Keluar dari Program - Pengguna dapat memilih untuk keluar dari program.

## Cara Menggunakan Program

1. Menjalankan Program:
- Pastikan Anda memiliki Python 3 terinstal di komputer Anda.
- Simpan file kode ini sebagai latihan3.py.
- Buka terminal atau command prompt, navigasikan ke folder tempat file latihan3.py disimpan, dan jalankan perintah berikut:

```python
python3 latihan3.py
```

2. Interaksi dengan Program:
- Menu Tarik Uang: Masukkan "1" dan kemudian masukkan jumlah penarikan. Program akan memvalidasi saldo dan mengurangi saldo sesuai dengan jumlah penarikan.
- Menu Keluar: Masukkan "2" untuk keluar dari program. Program akan menampilkan pesan perpisahan sebelum keluar.

## Penjelasan Kode

## 1. Inisialisasi Saldo

```python
saldo = 1000000
```

Saldo awal pengguna diatur sebesar Rp 1.000.000

## 2. Fungsi tampilkan_menu

```python
def tampilkan_menu():
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")
```

Fungsi ini menampilkan saldo pengguna dan dua opsi: Tarik Uang dan Keluar.

## 3. Loop Utama

Program menggunakan loop while yang berjalan terus-menerus hingga pengguna memilih untuk keluar.

- Pilihan 1 (Tarik Uang): Program meminta jumlah uang yang ingin ditarik. Jika jumlah yang diminta lebih besar dari saldo, program menampilkan pesan bahwa saldo tidak mencukupi. Jika saldo mencukupi, saldo dikurangi sesuai jumlah penarikan dan ditampilkan pesan "Penarikan berhasil!".

- Pilihan 2 (Keluar): Program akan menampilkan pesan terima kasih dan menghentikan loop, sehingga program berakhir.

- Input Tidak Valid: Jika pengguna memasukkan pilihan selain "1" atau "2", program akan menampilkan pesan error dan meminta pengguna untuk memasukkan pilihan yang valid.

## Contoh Output

Berikut adalah contoh tampilan saat program berjalan

```python
Saldo saat ini: Rp 1000000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 1
Masukkan jumlah penarikan: 500000
Penarikan berhasil!

Saldo saat ini: Rp 500000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 2
Terima kasih telah menggunakan ATM!
```

- Pada contoh ini: Pengguna memilih opsi "Tarik Uang" dan memasukkan jumlah penarikan Rp 500.000. Program berhasil melakukan penarikan dan mengurangi saldo. Pengguna kemudian memilih opsi "Keluar" untuk mengakhiri program.

## Berikut adalah hasin screenshot vsc


































 

