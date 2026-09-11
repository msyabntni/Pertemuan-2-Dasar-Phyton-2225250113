# Konstanta tahun sekarang
TAHUN_SEKARANG = 2026

# Meminta input dari pengguna
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

# Menghitung perkiraan umur
umur = TAHUN_SEKARANG - tahun_lahir
# Menampilkan kartu biodata
print()
print(f"Nama : {nama}")
print(f"NIM  : {nim}")
print(f"Kelas: {kelas}")
print(f"Umur : sekitar {umur} tahun")