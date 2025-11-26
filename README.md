def tampilkan_hasil(hasil):
    """Menampilkan hasil akhir perhitungan ke layar."""
    if hasil is not None:
        print("Hasil:", hasil)
    else:
        print("Tidak ada hasil yang bisa ditampilkan.")
# Memanggil semua functiom
if _name_ == "_main_":
    angka = ambil_angka()
    angka = tambah_angka_tambahan(angka)
    operasi = pilih_operator()
    hasil = hitung(angka, operasi)
    print("\n=== HASIL AKHIR ===")
    print("Hasil:", hasil)
