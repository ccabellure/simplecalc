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
