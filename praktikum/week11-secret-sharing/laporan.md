# Laporan Praktikum Kriptografi
Minggu ke-: XI  
Topik: Secret Sharing (Shamir’s Secret Sharing)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Secret Sharing (Shamir's Secret Sharing) adalaha salah satu skema kriptografi yang digunakan untuk membagi sebuah informasi  rahasia (secret) menjadi beberapa bagian yang disebut shares. Setiap share dibagikan kepada pihak yang berbeda, sehingga tidak ada satu pihak pun yang dapat mengetahui rahasia secara utuh. Rahasia tersebut hanya dapat direkonstruksi kembali apabiila sejumlah minimum share (threshold) dikumpulkan bersama, sesuai dengan ketentuan yang telah di tetapkan.

Skema Shamir's Secret Sharing bekerja berdasakan konsep matematika polinomial. Rahasia direpresentasikan sebagai konstanta pada sebuah polinomial berderajat tertentu, kemudian nilai share dihasilkan dari evaluasi polinomial tersebut pada beberapa titik berbeda. Keamanan metode ini terletak pada fakta bahwa tanpa jumlah share yang memenuhi threshold, sangat tidak mungkin untuk menebak atau merekonstruksi polinomoal sehingga rahasia tetap terlindungi. 

Shamir's Secret Sharing banyak digunakan dalam sistem keamanan dan manajemen kunci, seperti penyimpanan kunci kriptografi, sistem backup terdistribusi, dan pengamanan data sensitif. Dengan pendekatan ini, risiko kehilangan atau penyalahgunaan rahasia dapat diminimalkan, karena kontrol terhadap rahasia tidak bergantung pada satu entitas saja, melainkan tersebar pada beberapa pihak terpercaya.

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
1. Langkah 1 — Implementasi Shamir Secret Sharing.
2. Langkah 2 — Simulasi Manual (Tanpa Library).
3. Langkah 3 — Analisis Keamanan.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# Membagi rahasia menjadi beberapa shares
shares = SecretSharer.split_secret(secret, 3, 5)

# Menggabungkan kembali shares untuk mendapatkan rahasia asli
recovered = SecretSharer.recover_secret(shares[:3]) ...
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
Skema *(k,n)* pada Shamir's Secret SHaring tetap aman meskipun sebagian *share* bocor karena secara matematis diperlukan minimal *k share* untuk merekonstruksi rahasia, sehingga kepemilikan kurang dari k  tidak memberikan informasi apapun tentang secret. 

Namun, jika threshold *k* ditetapkan terlalu kecil, risiko keamanan meningkat karena rahasia dapat direkonstruksi dengan mudah ketika hanya sedikit *share* yang bocor atau disalahgunakan, sedangkan jika *k*  terlalu besar, risiko operasional muncul karena rahasia menjadi sulit dipulihkan ketika beberapa *share* hilang atau pemegang *share* tidak tersedia. 

Dalam penerapan dunia nyata, Shamir's Secret Sharing banyak digunakan pada manajemen kunci cryptocurrency dengan membagi *private key* ke beberapa pihak, pada sistem *recovery password* atau *account recovery* tanpa menyimpan password utuh di satu tempat, serta pada penyimpanan kunci enkripsi di lingkungan terdistribusi untuk meningkatkan keamanan dan keandalan sistem.


(Jawaban pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Keuntungan utama Shamir Secret Sharing adalah keamanan yang lebih tinggi, karena rahasia tidak pernah disimpan atau dibagikan dalam bentuk untuh, setiap *share* secara individual tidak bermakna dan tidak dapat digunakan tanpa mencapai jumlah minimum (*threshold*), berbeda dengan membagikan salinan kunci langsung yang berisiko bocor jika satu salinan jatuh ke pihak tidak berwenang. 
- Pertanyaan 2: Threshold (*k*) berperan sebagai batas minimum jumlah share yang harus digabungkan untuk merekonstruksi rahasia, sehingga menentukan tingkat keamanan dan keandalan sistem: semakin tepat nilai *k* ditetapkan, semakin seimbang antara perlindungan dari kebocoran (kurang dari *k* share tidak memberi informasi apapun) dan kemudahan pemulihan rahasia.  
- Pertanyaan 3: Salah satu contoh nyata penerapan Shamir's Secret Sharing adalah pada manajemen kunci dompet  cryptocurrency, dimana *private key* dibagi menjadi beberapa *share* dan disimpan oleh pihak atau perangkat yang berbeda, sehingga kunci hanya dapat dipulihkan jika jumlah minimum *share* (threshold) digabungkan, sekaligus mencegah kehilangan aset akibat satu titik kegagalan atau kebocoran kunci.  
)
---

## 8. Kesimpulan
Kode program ini berhasil mengimplementasikan Shamir's Secret Sharing dengan membagi rahasia ke dalam beberapa *share* menggunakan polinomial modulo bilangan prima bsar, sehingga setiap *share* tidak mengungkapka informasi rahasia secara langsung. Rahasia hanya dapat direkonstruksi kembali menggunakan minimal jumlah share sesuai threshold (k) melalui interpolasi Lagrange, yang membuktikan bahwa program berjalan efektif dalam menjaga keamanan rahasia

---
