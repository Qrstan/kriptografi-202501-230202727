# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Teori cipher klasik merupakan fondasi untuk kemajuan kriptografi kontemporer yang bertujuan menyandikan pesan agar tidak dapat diakses oleh orang yang tidak memiliki izin. Cipher klasik beroperasi dengan menggunakan dua prinsip, yaitu substitusi dan transposisi. Pada jenis substitusi, setiap karakter dalam teks asli digantikan dengan karakter lain berdasarkan aturan yang ditetapkan, contohnya adalah Caesar Cipher atau Vigenère Cipher. Sementara itu, untuk cipher transposisi, urutan huruf dalam pesan disusun kembali mengikuti pola tertentu tanpa mengubah hurufnya, seperti yang dilakukan pada Rail Fence Cipher atau Columnar Transposition Cipher.

Sasaran utama dari cipher klasik adalah melindungi kerahasiaan data melalui pengacakan simbol yang menyembunyikan makna sebenarnya. Namun, karena memanfaatkan pola dan ruang kunci yang terbatas, cipher klasik rentan terhadap serangan menggunakan analisis frekuensi, yang merupakan teknik untuk mengevaluasi seberapa sering karakter tertentu muncul guna memperkirakan pola enkripsi. Meskipun dianggap lemah dalam hal keamanan saat ini, teori cipher klasik tetap memiliki relevansi sebagai dasar konseptual dalam memahami prinsip-prinsip dasar enkripsi dan dekripsi, yang selanjutnya dikembangkan menjadi sistem kriptografi modern dengan tingkat keamanan yang jauh lebih tinggi.

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
1. Membuat file `caesar.py`, `transpose.py`, `vigenere.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar.py`, `transpose.py`, `vigenere.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# potongan kode
def caesar_encrypt(plaintext, key):
    result = "" 

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

def vigenere_encrypt(plaintext, key):
    result = []

def vigenere_decrypt(ciphertext, key):
    result = []

def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key

def transpose_decrypt(ciphertext, key=5):
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Kelemahan utama dari Caesar Cipher terletak pada rendahnya tingkat keamanannya, karena hanya ada 25 kemungkinan perpindahan. Hal ini membuatnya rentan terhadap pemecahan melalui teknik brute force atau analisis frekuensi huruf, sehingga tidak layak untuk menyimpan pesan rahasia.

Sementara itu, Vigenère Cipher memiliki masalah dengan penggunaan kunci yang berulang. Jika panjang kunci dapat diketahui atau cukup pendek, metode ini bisa dipecahkan dengan menganalisis frekuensi pola huruf (misalnya dengan Kasiski atau tes Friedman). Oleh karena itu, meskipun lebih kuat dibandingkan dengan Caesar, algoritma ini tetap memiliki kekurangan terhadap serangan kriptanalisis.

- Pertanyaan 2: Cipher klasik rentan terhadap analisis frekuensi karena pola penggunaan huruf dalam suatu bahasa tetap nampak meskipun teks telah diproses. Dalam bahasa seperti Indonesia atau Inggris, beberapa huruf (seperti “E” atau “A”) muncul lebih dominan dibanding yang lain. Cipher kuno seperti Caesar dan Vigenère tidak mengubah pola frekuensi ini dengan cara yang berarti, sehingga penyerang dapat membandingkan distribusi huruf dari ciphertext dengan pola bahasa yang sebenarnya untuk menebak huruf-huruf tersebut dan pada akhirnya memecahkan pesan yang tersembunyi.

- Pertanyaan 3: Cipher substitusi dan cipher transposisi memiliki perbedaan signifikan dalam metode enkripsi pesan mereka. Cipher substitusi berfungsi dengan menggantikan setiap karakter dalam teks asli dengan karakter lain. Kelebihan dari metode ini adalah kemudahan dalam penerapannya serta kemampuannya menciptakan ciphertext yang terlihat acak. Namun, kelemahannya terletak pada fakta bahwa pola frekuensi huruf dalam bahasa aslinya masih dapat dikenali, sehingga jenis cipher ini rentan terhadap analisis frekuensi, terutama ketika teks yang dienkripsi cukup panjang. 
Di sisi lain, cipher transposisi mengenkripsi pesan melalui perubahan urutan karakter tanpa merubah bentuk karakter itu sendiri. Keuntungannya adalah membuat pola pengurutan huruf jadi lebih susah untuk ditebak, sehingga sedikit lebih menantang untuk dipecahkan dibandingkan cipher substitusi yang sederhana. Namun, cipher transposisi juga memiliki kelemahan terkait kompleksitas proses enkripsi dan dekripsi, serta masih bisa rentan terhadap analisis pola jika kunci yang digunakan tidak cukup rumit atau saat pesan yang dienkripsi terlalu panjang.
)
---

## 8. Kesimpulan

Berdasarkan kegiatan praktikum pada minggu kelima mengenai Cipher Klasik, dapat disimpulkan bahwa algoritma Caesar, Vigenère, dan Transposisi adalah metode mendasar dalam bidang kriptografi yang dirancang untuk menyandikan informasi agar tidak dapat dengan mudah diakses oleh pihak-pihak yang tidak memiliki otorisasi. Dari hasil eksperimen, ketiga algoritma ini terbukti dapat melakukan enkripsi dan dekripsi dengan akurat sesuai dengan teori yang ada. Namun, dikarenakan pola enkripsi yang masih tergolong sederhana dan batasan ruang kunci yang ada, cipher klasik memiliki kelemahan yang cukup besar terhadap serangan analisis frekuensi, sehingga tidak disarankan untuk diterapkan dalam konteks keamanan saat ini, tetapi tetap memiliki relevansi yang penting sebagai fondasi pemahaman mengenai konsep kriptografi.
---



