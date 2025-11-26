def ambil_angka():
    """Meminta input dari pengguna untuk dua angka pertama yang akan dihitung."""
    return [float(input("Angka pertama: ")), float(input("Angka kedua: "))]

def tambah_angka_tambahan(daftar_angka):
    """Menanyakan apakah pengguna ingin menambah satu angka lagi"""
    pilihan = int(input("Apakah mau menambah satu angka lagi? (1=Ya, 2=Tidak): "))
    if pilihan == 1:
        angka_baru = float(input("Masukkan angka tambahan: "))
        daftar_angka.append(angka_baru)
    elif pilihan != 2:
        print("Pilihan tidak valid. Tidak ada angka yang ditambahkan.")
    return daftar_angka

def pilih_operator():
    """Meminta pengguna memilih operator yang akan digunakan."""
    operasi = int(input("""Pilih operator:
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
Pilihan: """))
    if operasi not in (1, 2, 3, 4):
        print("Pilihan tidak valid. Menggunakan penjumlahan sebagai default.")
        operasi = 1
    return operasi

def hitung(daftar_angka, operasi):
    """Melakukan perhitungan sesuai operator yang dipilih."""
    if operasi == 1:
        hasil = sum(daftar_angka)
    elif operasi == 2:
        hasil = daftar_angka[0]
        for angka in daftar_angka[1:]:
            hasil -= angka
    elif operasi == 3:
        hasil = 1
        for angka in daftar_angka:
            hasil *= angka
    elif operasi == 4:
        hasil = daftar_angka[0]
        for angka in daftar_angka[1:]:
            if angka == 0: # Mencegah pembagian dengan 0
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                return None
            hasil /= angka
    else:
        print("Operasi tidak valid.")
        hasil = None
    return hasil

def tampilkan_hasil(hasil):
    """Menampilkan hasil akhir perhitungan ke layar."""
    if hasil is not None:
        print("Hasil:", hasil)
    else:
        print("Tidak ada hasil yang bisa ditampilkan.")
# Memanggil semua functiom
if __name__ == "__main__":
    angka = ambil_angka()
    angka = tambah_angka_tambahan(angka)
    operasi = pilih_operator()
    hasil = hitung(angka, operasi)
    print("\n=== HASIL AKHIR ===")
    print("Hasil:", hasil)
