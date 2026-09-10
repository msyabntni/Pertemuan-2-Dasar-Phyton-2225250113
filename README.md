# Identitas

**Nama:** Masya Bantani  
**NIM:** 2225250113 
**Kelas:** 3E
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** Pendidikan Matematika  
**Universitas:** Universitas Sultan Ageng Tirtayasa (UNTIRTA)

## Tujuan Repository

Repository ini dibuat untuk menyimpan dan mendokumentasikan hasil latihan pemrograman Python pada mata kuliah Algoritma dan Pemrograman.

Melalui repository ini, mahasiswa dapat:
- Mempraktikkan dasar-dasar pemrograman Python.
- Memahami penggunaan input dan output.
- Menerapkan variabel, konstanta, dan tipe data.
- Menggunakan operasi aritmatika dalam program.
- Melakukan pengujian program dengan beberapa contoh input.
- Mendokumentasikan hasil latihan menggunakan GitHub.

- ## Daftar Berkas dan Fungsi

| No. | Berkas | Fungsi |
|---|---|---|
| 1 | `latihan/01_biodata.py` | Membuat program biodata dengan input nama, NIM, kelas, dan tahun lahir serta menghitung perkiraan umur. |
| 2 | `latihan/02_persegi_panjang.py` | Menghitung luas dan keliling persegi panjang berdasarkan panjang dan lebar yang dimasukkan pengguna. |
| 3 | `latihan/03_konversi_suhu.py` | Mengonversikan suhu dari Celsius ke Fahrenheit dan Kelvin. |
| 4 | `README.md` | Berisi identitas, tujuan repository, daftar berkas, penjelasan program, dan hasil pengujian. |

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di komputer.
2. Buka folder repository menggunakan Visual Studio Code.
3. Buka Terminal di VS Code.
4. Jalankan salah satu file Python dengan perintah berikut:

### Latihan 1 - Biodata

```bash
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py

Kalau **khusus Latihan 3**, bagian README-nya bisa dibuat lebih singkat:

```markdown
## Cara Menjalankan Program

1. Buka repository menggunakan Visual Studio Code.
2. Buka Terminal.
3. Jalankan perintah:

```bash
python latihan/03_konversi_suhu.py

## Hasil Pengujian Utama

Pengujian dilakukan menggunakan dua nilai Celsius, yaitu 0°C dan 100°C. Hasil program kemudian dibandingkan dengan perhitungan manual.

| No. | Input | Output Fahrenheit | Output Kelvin | Hasil Pengujian |
|---|---:|---:|---:|---|
| 1 | 0°C | 32.00°F | 273.15 K | Berhasil |
| 2 | 100°C | 212.00°F | 373.15 K | Berhasil |

Berdasarkan pengujian, hasil konversi dari program sesuai dengan hasil perhitungan manual.

## Refleksi

Dari latihan konversi suhu ini, saya belajar menggunakan input dengan tipe data `float`, membuat konstanta, serta menerapkan rumus matematika ke dalam program Python. Saya juga belajar bahwa hasil program perlu diuji menggunakan beberapa nilai dan dibandingkan dengan perhitungan manual untuk memastikan program berjalan dengan benar.

Latihan ini membantu saya lebih memahami hubungan antara rumus matematika dan cara menerapkannya dalam bahasa pemrograman Python.
## Sumber yang Digunakan

1. Modul/Bahan Ajar Mata Kuliah Algoritma dan Pemrograman.
2. Dokumentasi resmi Python untuk fungsi `input()`, tipe data `float`, konstanta, dan f-string.
3. Materi pembelajaran mengenai konversi suhu Celsius, Fahrenheit, dan Kelvin.
