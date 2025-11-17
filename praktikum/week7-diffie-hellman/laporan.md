# Laporan Praktikum Kriptografi
Minggu ke-: VII  
Topik: Diffie-Hellman Key Exchange  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Mekanisme Diffie-Hellman adalah protokol pertukaran kunci yang memungkinkan dua pihak menghasilkan sebuah kunci rahasia bersama melalui jaringan yang tidak  aman, tanpa harus saling mengirimkan kunci rahasia tersebut secara langsung. Protokol ini bekerja dengan memanfaatkan sifat matematika eksponen modulo bilangan prima. Dua nilai publik, yaitu bilangan prima besar *p* dan generator *g*, gadapat diketahui siapa saja tanpa menimbulkan risiko keamanan.

Setiap piiak memilih unci privat secara acak, misalnya Alice memilih *a* dab Bob memilih *b*. Mereka kemudian menghitung kunci publik masing-masing, yaitu *A = g^a* mod *p* dan *B = g^b* mod *p*, lalu saling menukarnya. Setelah menerima kunci pubik dari lawan, mereka menghitung kunci bersama: Alice menghitung *B^a* mod *p* dan Bob menghitung *A^b* mod *P*. Secara matematika, kedua hasil tersebut sama, karena *g^ab* mod *p = g^gba* mod *P*. 

Keamanan Diffie-Hellman bergantung pada kesulitan Discrete Logarithm Problem, yaitu sulitnya menurunkan nilai *a* dari *A = G^a* mod *P* ketika *P* sangat besar. Walaupun nilai *p, g, A, dan B bersifat publik, pihak ketiga tidak dapat dengan mudah menghitung kunci rahasia bersama tanpa mengetahui kunci privat masing-masing pihak. 
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
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

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
- Pertanyaan 1: Diffie–Hellman memungkinkan pertukaran kunci di saluran publik karena hanya nilai publik seperti 𝑝, 𝑔, dan kunci publik yang dikirimkan, sementara kunci rahasia tidak pernah dibagikan. Keamanannya bergantung pada sulitnya Discrete Logarithm Problem, sehingga meskipun penyerang melihat semua nilai publik, mereka tetap tidak dapat menghitung kunci rahasia bersama.  
- Pertanyaan 2: Kelemahan utama protokol Diffie–Hellman murni adalah tidak adanya autentikasi. Artinya, protokol ini tidak dapat memastikan bahwa pihak yang diajak bertukar kunci benar-benar pihak yang dimaksud. Akibatnya, protokol ini rentan terhadap serangan Man-in-the-Middle (MitM), di mana penyerang dapat menyisipkan dirinya di antara dua pihak, membuat dua kunci berbeda, dan membaca seluruh komunikasi tanpa terdeteksi.  
- Pertanyaan 3: Serangan MITM pada Diffie–Hellman dapat dicegah dengan menambahkan autentikasi pada proses pertukaran kunci. Cara umum adalah memakai tanda tangan digital untuk menandatangani kunci publik sehingga pihak lain bisa memverifikasinya dan memastikan tidak ada penyusupan. Selain itu, penggunaan sertifikat digital (PKI) membuat kunci publik divalidasi oleh otoritas tepercaya. Banyak protokol modern juga memakai Authenticated Diffie–Hellman, seperti ECDHE pada TLS, yang menggabungkan Diffie–Hellman dengan sertifikat server sehingga penyerang tidak dapat menyamar dan mengubah kunci publik di tengah proses.  
)
---

## 8. Kesimpulan
Berdasarkan percobaan, protokol Diffie–Hellman berhasil menghasilkan kunci rahasia bersama yang sama pada kedua pihak meskipun dilakukan melalui saluran publik. Mekanisme pertukaran kunci ini terbukti bergantung pada operasi eksponen modulo dan keamanan Discrete Logarithm Problem. Namun, Diffie–Hellman murni tetap membutuhkan autentikasi tambahan untuk mencegah serangan Man-in-the-Middle.
---

