Judul Program:
Kalkulator Operasi Matematika Sederhana (Python CLI Calculator)

Pendahuluan:
Program ini merupakan kalkulator berbasis Command Line Interface (CLI) yang memungkinkan pengguna melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian.
Pengguna dapat memasukkan dua angka awal, kemudian memilih apakah ingin menambah satu angka tambahan sebelum memilih operator perhitungan. Program ini dirancang untuk latihan modularisasi fungsi dan interaksi input pengguna dalam Python.

Fitur Utama:
	•	Input dua angka pertama untuk melakukan operasi matematika.
	•	Opsional menambah angka ketiga sesuai kebutuhan pengguna.
	•	Pilihan operator lengkap:
	•	Penjumlahan
	•	Pengurangan
	•	Perkalian
	•	Pembagian
	•	Validasi input operator (default ke penjumlahan jika pilihan salah).
	•	Perlindungan pembagian dengan nol.
	•	Struktur program modular menggunakan beberapa fungsi:
	•	ambil_angka()
	•	tambah_angka_tambahan()
	•	pilih_operator()
	•	hitung()
	•	tampilkan_hasil()

Panduan Instalasi:
Langkah-langkah untuk menjalankan program pada komputer Anda:
	1.	Clone repository menggunakan Git:
git clone <link-repository-github-anda>
	2.	Masuk ke folder project:
cd nama-folder-project
	3.	Pastikan Python sudah terinstall (versi 3.x):
python --version
Tidak ada library eksternal yang perlu diinstall karena program hanya menggunakan fungsi bawaan Python.

Panduan Menjalankan Program:
	1.	Jalankan program melalui terminal/command prompt:
python nama_file.py
	2.	Ikuti instruksi di layar:
	•	Masukkan angka pertama
	•	Masukkan angka kedua
	•	Pilih apakah ingin menambah angka ketiga
	•	Pilih operator perhitungan (1–4)
	3.	Program akan menampilkan HASIL AKHIR sesuai operasi yang dipilih.
Contoh tampilan:
Angka pertama: 10
Angka kedua: 5
Apakah mau menambah satu angka lagi? (1=Ya, 2=Tidak): 1
Masukkan angka tambahan: 2
Pilih operator:
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
Pilihan: 1
=== HASIL AKHIR ===
Hasil: 17

Dokumentasi Teknis:
[Klik untuk membuka flowchart](flowchart kalkulator simple drawio.pdf)
Penjelasan Modul Utama
	•	fungsi ambil_angka()
Mengambil dua angka pertama dari pengguna.
	•	fungsi tambah_angka_tambahan(daftar_angka)
Menambah satu angka lagi jika pengguna memilih “Ya”.
	•	fungsi pilih_operator()
Meminta input operator dengan validasi pilihan.
	•	fungsi hitung(daftar_angka, operasi)
Menjalankan proses hitung berdasarkan operator:
	•	Penjumlahan → sum()
	•	Pengurangan → looping pengurangan
	•	Perkalian → looping perkalian
	•	Pembagian → looping pembagian + pengecekan pembagian nol
	•	fungsi tampilkan_hasil(hasil)
Menampilkan hasil akhir ke layar.

Daftar Kontributor:
