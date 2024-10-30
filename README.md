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




## Penjelasan Kode






















 

