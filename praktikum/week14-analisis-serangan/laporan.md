# Laporan Praktikum Kriptografi
Minggu ke-: XIV 
Topik: [Analisis Serangan Kriptografi]  
Nama: [Hartanti]  
NIM: [230202727]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Studi kasus yang dianalisis pada praktikum ini adalah kebocoran SSL/TLS pada sistem komunikasi berbasis web. Kebocoran ini memungkinkan terjadinya penyadapan data melalui serangan Man-in-the-Middle (MITM), di mana penyerang dapat mencegat komunikasi antara klien dan server. Serangan ini umumnya terjadi akibat penggunaan protokol SSL/TLS versi lama, algoritma kriptografi yang sudah tidak aman, serta lemahnya validasi sertifikat digital pada sistem, sehingga data sensitif seperti kredensial pengguna berpotensi bocor meskipun koneksi terlihat terenkripsi.

Evaluasi menunjukkan bahwa kelemahan sistem tidak hanya berasal dari algoritma kriptografi, tetapi juga dari aspek implementasi dan konfigurasi. Dari sisi algoritma, penggunaan hash lemah seperti MD5 atau SHA-1 rentan terhadap serangan collision dan tidak lagi memenuhi standar keamanan saat ini. Dari sisi implementasi dan konfigurasi, kesalahan seperti tidak memverifikasi sertifikat server secara ketat serta masih mengaktifkan cipher suite dan protokol lama membuka peluang terjadinya downgrade attack dan serangan MITM.

Sebagai rekomendasi solusi, sistem perlu diperbarui dengan menggunakan TLS versi terbaru (minimal TLS 1.2 dan direkomendasikan TLS 1.3) serta mengganti algoritma kriptografi lama dengan algoritma yang lebih aman, seperti SHA-256 untuk fungsi hash dan Elliptic Curve Cryptography (ECC) untuk pertukaran kunci. Selain itu, penyimpanan password dalam bentuk plaintext harus dihindari dan digantikan dengan algoritma bcrypt, scrypt, atau Argon2. Penerapan solusi ini akan meningkatkan keamanan komunikasi data dan meminimalkan risiko kebocoran informasi pada sistem.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Identifikasi Serangan
2. Evaluasi Kelemahan
3. Rekomendasi Solusi)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

wordlist = ["123456", "admin", "qwerty", "password", "iloveyou"]

for word in wordlist:
    hash_word = hashlib.md5(word.encode()).hexdigest()
    print(f"Mencoba: {word} -> {hash_word}")

    if hash_word == target_hash:
        print(f"\n[✓] Password ditemukan: {word}")
        break
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
- Pertanyaan 1: Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena menggunakan mekanisme autentikasi dan algoritma kriptografi yang sudah tidak lagi memenuhi standar keamanan saat ini. Contohnya adalah penggunaan password yang lemah, penyimpanan password dalam bentuk plaintext atau hash tanpa salt, serta penggunaan algoritma hash lama seperti MD5 atau SHA-1. Selain itu, sistem lama umumnya tidak menerapkan pembatasan percobaan login (rate limiting) dan mekanisme penguncian akun, sehingga penyerang dapat mencoba berbagai kombinasi password secara berulang tanpa hambatan berarti.

- Pertanyaan 2: Perbedaan antara kelemahan algoritma dan kelemahan implementasi terletak pada sumber permasalahannya. Kelemahan algoritma muncul ketika suatu algoritma kriptografi secara matematis telah terbukti tidak aman, misalnya rentan terhadap serangan collision atau kriptanalisis tertentu. Sementara itu, kelemahan implementasi terjadi ketika algoritma yang sebenarnya aman diterapkan dengan cara yang salah, seperti penggunaan kunci yang terlalu pendek, manajemen kunci yang buruk, atau tidak adanya verifikasi sertifikat pada sistem SSL/TLS. Dengan kata lain, algoritma yang kuat sekalipun dapat menjadi tidak aman jika diimplementasikan secara keliru.

- Pertanyaan 3: Untuk memastikan sistem kriptografi tetap aman di masa depan, organisasi perlu melakukan pembaruan dan evaluasi keamanan secara berkala. Hal ini mencakup penggunaan algoritma dan protokol terbaru yang direkomendasikan oleh standar keamanan, penerapan konfigurasi sistem yang ketat, serta audit keamanan secara rutin. Selain itu, organisasi perlu mengikuti perkembangan riset kriptografi dan ancaman keamanan terbaru, serta menerapkan prinsip secure by design dan defense in depth. Dengan pendekatan ini, sistem kriptografi dapat tetap adaptif dan tahan terhadap serangan yang terus berkembang.  
)
---

## 8. Kesimpulan
(Berdasarkan percobaan dan analisis yang dilakukan, kebocoran SSL/TLS dapat terjadi akibat penggunaan algoritma kriptografi yang lemah serta kesalahan implementasi dan konfigurasi sistem. Sistem yang masih menggunakan protokol lama dan algoritma tidak aman terbukti lebih rentan terhadap serangan seperti Man-in-the-Middle dan penyadapan data. Oleh karena itu, pembaruan algoritma kriptografi dan penerapan konfigurasi keamanan yang tepat menjadi langkah penting untuk meningkatkan perlindungan sistem  )

---
