# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Public Key Infrastructure (PKI & Certificate Authority)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sebuah sistem yang menyediakan mekanisme untuk mengelola pasangan kunci publik–privat, sekaligus memastikan keaslian identitas dalam komunikasi digital. PKI bekerja dengan konsep kriptografi kunci publik, di mana kunci privat digunakan untuk menandatangani data, sedangkan kunci publik digunakan untuk melakukan verifikasi. Agar kunci publik dapat dipercaya, PKI menggunakan sertifikat digital—dokumen elektronik yang memuat informasi identitas pemilik kunci publik, algoritma yang digunakan, masa berlaku, serta tanda tangan digital dari pihak yang menerbitkan sertifikat.

Certificate Authority (CA) adalah lembaga atau entitas terpercaya yang berperan menerbitkan serta menandatangani sertifikat digital. CA memastikan bahwa kunci publik benar-benar milik entitas yang mengklaim identitas tersebut. Proses ini dilakukan melalui mekanisme verifikasi identitas (certificate signing) sebelum sertifikat diterbitkan. Karena CA menandatangani sertifikat menggunakan kunci privatnya sendiri, siapa pun dapat memverifikasi keasliannya menggunakan kunci publik CA yang telah disimpan pada sistem operasi atau browser.

Secara keseluruhan, PKI memungkinkan komunikasi aman melalui enkripsi, integritas, dan autentikasi, terutama pada protokol seperti TLS/HTTPS. Ketika pengguna membuka situs web HTTPS, browser akan memeriksa apakah sertifikat digital situs tersebut valid dan ditandatangani oleh CA terpercaya. Jika sertifikat tidak valid atau diterbitkan oleh CA palsu, browser akan menampilkan peringatan keamanan. Dengan demikian, PKI berperan penting dalam mencegah serangan seperti Man-in-the-Middle (MITM), menjaga privasi pengguna, dan memastikan kepercayaan dalam transaksi digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
1. Membuat Sertifikat Digital Sederhana
2. Memverifikasi Sertifikat.
3. Analisis PKI

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
Diskusi kasus nyata:
- Pertanyaan 1: Browser memverifikasi sertifikat HTTPS dengan memeriksa apakah sertifikat tersebut ditandatangani oleh Certificate Authority (CA) yang ada dalam daftar CA terpercaya. Saat situs HTTPS diakses, server mengirimkan sertifikatnya, lalu browser mengecek tanda tangan digital, kecocokan nama domain, masa berlaku, serta status pencabutan sertifikat. Jika semua valid, browser menampilkan koneksi aman; jika tidak, muncul peringatan bahwa situs tidak dapat dipercaya.
  
- Pertanyaan 2: Jika CA palsu menerbitkan sertifikat, penyerang dapat membuat situs yang terlihat resmi dan melakukan penyamaran. Hal ini memungkinkan serangan Man-in-the-Middle (MITM), karena browser akan mengira situs tersebut valid. Akibatnya, data pengguna seperti password, transaksi, atau informasi sensitif bisa dicuri. Inilah sebabnya hanya CA terpercaya yang boleh mengeluarkan sertifikat.
  
- Pertanyaan 3: PKI penting dalam komunikasi aman karena memastikan tiga hal utama: autentikasi, kerahasiaan, dan integritas data. Dengan sertifikat digital dan kunci publik, PKI membantu memastikan bahwa pengguna benar-benar terhubung ke server yang asli, bukan situs palsu. Selain itu, PKI memungkinkan enkripsi data sehingga informasi sensitif—seperti password atau detail transaksi—tetap aman saat dikirim. Karena itu, PKI menjadi fondasi keamanan untuk transaksi online, login, dan komunikasi berbasis HTTPS.

pertanyaan diskusi:
- Pertanyaan 1: Fungsi utama Certificate Authority (CA) adalah memverifikasi identitas pihak yang mengajukan sertifikat digital dan menerbitkan sertifikat tersebut. CA menjamin bahwa kunci publik dalam sertifikat benar-benar milik entitas yang sah, sehingga komunikasi digital dapat berlangsung secara aman dan terpercaya.

- Pertanyaan 2: Self-signed certificate tidak cukup untuk sistem produksi karena tidak diverifikasi oleh Certificate Authority (CA) terpercaya. Akibatnya, browser atau sistem tidak dapat memastikan keaslian identitas server dan akan menampilkan peringatan keamanan. Hal ini berisiko menurunkan kepercayaan pengguna dan membuka peluang serangan seperti Man-in-the-Middle (MITM).
 
- Pertanyaan 3: PKI mencegah serangan MITM dengan memastikan identitas server melalui sertifikat digital yang ditandatangani oleh Certificate Authority (CA) terpercaya. Browser memverifikasi sertifikat tersebut sebelum membangun koneksi TLS, sehingga penyerang tidak dapat menyamar sebagai server tanpa sertifikat yang valid. Selain itu, enkripsi TLS memastikan data yang dikirim tidak dapat dibaca atau diubah oleh pihak ketiga.  
)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, program Python berhasil menghasilkan sertifikat digital self-signed menggunakan algoritma RSA 2048 bit dan library cryptography. Sertifikat disimpan dalam format PEM (cert.pem) dan menunjukkan bagaimana konsep dasar Public Key Infrastructure (PKI) bekerja. Percobaan ini membuktikan peran sertifikat digital dalam mendukung autentikasi dan komunikasi yang aman. )

---


