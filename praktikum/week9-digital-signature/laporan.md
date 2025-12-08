# Laporan Praktikum Kriptografi
Minggu ke-: IX  
Topik: igital Signature (RSA/DSA)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5 IKRA  

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
Digital signature atau tanda tangan digital adalah mekanisme kriptografi yang menjamin keaslian (authentication), integritas, dan non-repudiation pada dokumen atau pesan elektronik. Dengan digital signature, penerima dapat memastikan bahwa pesan benar berasal dari pengirim yang sah dan tidak berubah selama transmisi. Proses ini memanfaatkan pasangan kunci publik dan privat seperti pada kriptografi asimetris serta fungsi hash satu arah untuk merangkum pesan menjadi message digest.

RSA dan DSA adalah dua algoritma digital signature yang paling umum digunakan. Pada RSA, kunci privat digunakan untuk menandatangani (mengenkripsi hash pesan) dan kunci publik digunakan untuk memverifikasi tanda tangan. Sementara itu, DSA (Digital Signature Algorithm) merupakan standar yang ditetapkan oleh NIST, bekerja berdasarkan kriptografi diskrit logaritma dan hanya digunakan untuk penandatanganan (bukan enkripsi data). Perbedaan utamanya: RSA bersifat lebih fleksibel dan dapat digunakan untuk enkripsi maupun tanda tangan, sedangkan DSA lebih efisien terutama pada proses verifikasi namun hanya untuk tanda tangan digital.

Keduanya memberikan jaminan bahwa jika tanda tangan valid, maka pesan tidak dimodifikasi dan benar berasal dari pemilik kunci privat. Digital signature sangat penting dalam keamanan sistem modern seperti e-commerce, sertifikat digital, aplikasi perbankan, dan komunikasi yang membutuhkan validasi identitas.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Langkah 1 — Generate Key dan Buat Tanda Tangan
Langkah 2 — Verifikasi Tanda Tangan
Langkah 3 — Uji Modifikasi Pesan
)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuan dan penggunaan kuncinya. Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan, di mana pengirim mengenkripsi menggunakan kunci publik penerima dan penerima mendekripsi dengan kunci privat. Sementara itu, tanda tangan digital RSA bertujuan memastikan keaslian, integritas, dan non-repudiation, yaitu pengirim menandatangani menggunakan kunci privatnya dan penerima memverifikasi dengan kunci publik. Dengan demikian, enkripsi fokus pada menjaga isi pesan tetap rahasia, sedangkan tanda tangan digital memastikan bahwa pesan asli berasal dari pengirim yang sah dan tidak mengalami perubahan.  
- Pertanyaan 2: Tanda tangan digital menjamin integritas dan otentikasi karena prosesnya melibatkan hash dan kunci privat pengirim. Hash memastikan bahwa setiap perubahan sekecil apa pun pada pesan akan menghasilkan nilai hash berbeda, sehingga penerima dapat mendeteksi jika pesan dimodifikasi. Sementara itu, penggunaan kunci privat untuk menandatangani memastikan bahwa hanya pemilik kunci privat tersebut yang dapat membuat tanda tangan tersebut, dan pihak penerima dapat memverifikasinya dengan kunci publik. Dengan kombinasi ini, tanda tangan digital dapat membuktikan bahwa pesan benar berasal dari pengirim yang sah dan tetap utuh selama proses pengiriman.  
- Pertanyaan 3: Certificate Authority (CA) berperan sebagai pihak ketiga tepercaya yang memverifikasi identitas pemilik kunci publik dalam sistem tanda tangan digital modern. CA menerbitkan sertifikat digital yang mengaitkan kunci publik dengan identitas pemiliknya setelah melalui proses validasi, sehingga penerima pesan dapat yakin bahwa kunci publik yang digunakan untuk verifikasi benar milik pengirim yang sah. Dengan demikian, CA membantu mencegah pemalsuan identitas serta memperkuat kepercayaan dalam komunikasi dan transaksi digital di berbagai layanan seperti HTTPS, e-commerce, dan sistem keamanan jaringan. 
)
---

## 8. Kesimpulan
Kesimpulan dari percobaan ini menunjukkan bahwa tanda tangan digital RSA hanya dapat diverifikasi jika pesan tidak diubah, sehingga integritas pesan terjamin. Selain itu, keberhasilan verifikasi menggunakan kunci publik membuktikan bahwa tanda tangan benar berasal dari pemilik kunci privat, sehingga otentikasi pengirim juga terjamin.

---

