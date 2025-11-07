# Laporan Praktikum Kriptografi
Minggu ke-: VI  
Topik: Cipher Modern (DES, AES, RSA)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
Algoritma kriptografi modern adalah prosedur matematika yang digunakan untuk mengamankan data dengan mengubah insformasi asli menjadi bentuk yang tidak dapat dibaca tanpa kunci khusus. Tujuannya adalah menjaga kerahasiaan, integritas, otentikasi, dan mencegah pengingkaran dalam komunikasi digiital. Dalam proosesnya, terdapat enkripsi untuk mengubah plaintex menjadi ciphertext serta dekripsi untuk mengembalikanya ke bentuk semula, dengan kunci sebagai elemen pending dalam kedua proses tersebut.

Kriptografi modern terbagi menjadi tiga jenis utama. Kriptografi simetris menggunakan satu kunci yang sama untuk enkripsi dan dekripsi, dengan contoh seperti AES yang cepat dan efisien. Kriptografi asimetris menggunakan pasangan kunci publik dan privat, seperti RSA dan ECC, yang mengatasi masalah distribusi kunci namun lebih lambat. Sementara itu, fungsi hash seperti SHA-256 digunakan untuk menghasilkan nilai tetap yang tidak dapat dibalik, sehingga berguna untuk menjaga integritas data dan tanda tangan digital.

Dalam praktiknya, algoritma seperti AES sering digunakan untuk enkripsi data utama karena kecepatanya, sedangkan RSA atau ECC digunakan untuk mengamankan pertukaran kunci. Kombinasi ini anyak diterapkan pada teknologi keamanan modern seperti HTTPS, VPN, aplikasi perbankan, dan sistem komunikasi. 

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
1. Membuat file `aes.py`, `rsa.py`,`des.py` di folder `praktikum/week6-cipher-modern/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `aes.py`, `rsa.py`,`des.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# potongan kode
from Crypto.Cipher import AES

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)...

# potongan kode
from Crypto.Cipher import PKCS1_OAEP

cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(plaintext)
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)...

# potongan kode
from Crypto.Cipher import DES

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(ciphertext)...

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
- Pertanyaan 1: Perbedaan mendasar antara DES, AES, dan RSA terletak pada jenis kunci dan tingkat keamanannya. DES dan AES adalah algoritma kriptografi simetris, artinya menggunakan kunci yang sama untuk enkripsi dan dekripsi. Namun, DES memiliki panjang kunci yang kecil (56 bit) sehingga mudah diserang, sedangkan AES memiliki kunci lebih panjang (128/192/256 bit) sehingga jauh lebih aman dan digunakan secara luas saat ini. Sementara itu, RSA adalah algoritma kriptografi asimetris yang menggunakan sepasang kunci (kunci publik dan kunci privat), biasanya digunakan untuk pertukaran kunci atau tanda tangan digital, dan meskipun lebih aman untuk autentikasi, RSA lebih lambat dibandingkan AES.
  
- Pertanyaan 2: AES lebih banyak digunakan dibanding DES karena AES memiliki tingkat keamanan yang jauh lebih tinggi serta kinerja yang lebih efisien. DES hanya menggunakan panjang kunci 56 bit, sehingga kini mudah dipecahkan dengan serangan brute force menggunakan komputer modern. Sebaliknya, AES menggunakan kunci 128, 192, atau 256 bit, sehingga jauh lebih sulit untuk diretas. Selain itu, AES dirancang untuk bekerja cepat pada perangkat keras maupun perangkat lunak, sehingga menjadi standar enkripsi modern untuk berbagai aplikasi seperti Wi-Fi, VPN, dan komunikasi data aman.
 
- Pertanyaan 3: RSA dikategorikan sebagai algoritma asimetris karena menggunakan dua kunci yang berbeda untuk proses enkripsi dan dekripsi, yaitu kunci publik dan kunci privat. Kunci publik dapat dibagikan secara bebas untuk mengenkripsi data, sedangkan kunci privat harus dijaga kerahasiaannya karena digunakan untuk mendekripsi data. Dengan demikian, tidak seperti kriptografi simetris yang memakai satu kunci yang sama, RSA memisahkan peran kunci untuk meningkatkan keamanan dalam pertukaran informasi.

Proses pembangkitan kunci RSA dimulai dengan memilih dua bilangan prima besar. Kedua prima tersebut dikalikan untuk membentuk modulus (n), yang menjadi dasar kekuatan RSA karena sulitnya memfaktorkan kembali hasil perkalian tersebut. Setelah itu, nilai eksponen publik (e) dipilih, kemudian dihitung nilai eksponen privat (d) sebagai kunci pasangannya. Hasil akhirnya adalah pasangan kunci (n, e) sebagai kunci publik dan (n, d) sebagai kunci privat, yang saling terkait secara matematis namun sulit diturunkan satu sama lain tanpa perhitungan yang sangat besar.
)
---

## 8. Kesimpulan

Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa algoritma kriptografi modern memiliki peran penting dalam menjaga keamanan data. DES, AES, dan RSA memiliki perbedaan pada penggunaan kunci dan tingkat keamanannya, di mana AES lebih aman dan efisien dibanding DES, sedangkan RSA digunakan untuk pertukaran kunci dengan sistem kunci publik dan privat. Melalui implementasi ketiga algoritma ini, dapat dipahami bahwa pemilihan algoritma bergantung pada kebutuhan keamanan dan efisiensi dalam proses enkripsi dan dekripsi data.


---
