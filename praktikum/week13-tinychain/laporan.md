# Laporan Praktikum Kriptografi
Minggu ke-: XIII  
Topik: TinyChain – Proof of Work (PoW)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
Blockchain merupakan teknologi buku besar terdistribusi (distributed ledger) yang menyimpan data transaksi dalam bentuk blok-blok yang saling terhubung menggunakan fungsi hash kriptografis. Keamanan blockchain bergantung pada prinsip kriptografi, desentralisasi, dan konsensus. Setiap blok berisi hash blok sebelumnya sehingga perubahan pada satu blok akan memengaruhi seluruh rantai, membuat manipulasi data menjadi sangat sulit. Selain itu, karena data disalin dan diverifikasi oleh banyak node dalam jaringan, tidak ada satu pihak pun yang dapat dengan mudah mengendalikan atau mengubah isi blockchain secara sepihak.

Proof of Work (PoW) adalah mekanisme konsensus yang digunakan untuk menjaga keamanan dan integritas blockchain dengan mewajibkan node (miner) memecahkan teka-teki kriptografis yang membutuhkan daya komputasi tinggi. Proses ini memastikan bahwa penambahan blok baru memerlukan usaha nyata (work), sehingga serangan seperti pemalsuan transaksi atau perubahan riwayat blockchain menjadi sangat mahal dan tidak efisien. PoW juga mencegah serangan spam karena setiap transaksi harus divalidasi melalui proses penambangan.

Dari sisi keamanan, PoW efektif dalam melindungi blockchain dari serangan seperti double spending dan modifikasi data, selama mayoritas kekuatan komputasi (lebih dari 50%) dikuasai oleh node yang jujur. Namun, PoW memiliki kelemahan berupa konsumsi energi yang tinggi dan potensi sentralisasi penambangan pada pihak dengan sumber daya besar. Oleh karena itu, meskipun PoW terbukti kuat secara keamanan, pengembang blockchain terus mengeksplorasi mekanisme konsensus alternatif yang lebih efisien tanpa mengorbankan aspek keamanan.


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
1. Membuat Struktur Blok
2. Membuat Blockchain
3. Analisis Proof of Work
)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
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
- Pertanyaan 1: Fungsi hash sangat penting dalam blockchain karena berperan sebagai mekanisme pengaman data. Hash mengubah data transaksi menjadi nilai unik dengan panjang tetap, sehingga setiap perubahan kecil pada data akan menghasilkan hash yang berbeda secara signifikan. Hal ini menjamin integritas data, memudahkan proses verifikasi blok, serta menghubungkan antarblok melalui previous_hash, sehingga perubahan pada satu blok akan merusak seluruh rantai.  
- Pertanyaan 2: Proof of Work (PoW) mencegah double spending dengan mewajibkan penambang melakukan komputasi yang mahal untuk memvalidasi dan menambahkan blok baru. Setiap transaksi hanya dianggap sah setelah masuk ke dalam blok yang berhasil ditambang dan terkonfirmasi oleh jaringan. Untuk mengubah atau menggandakan transaksi, penyerang harus mengulang proses PoW pada blok tersebut dan seluruh blok setelahnya, yang secara komputasi hampir tidak mungkin dilakukan tanpa menguasai mayoritas daya komputasi jaringan.  
- Pertanyaan 3: Kelemahan PoW dalam hal efisiensi energi terletak pada kebutuhan komputasi yang sangat tinggi. Proses pencarian nonce menyebabkan banyak percobaan hash yang sebagian besar sia-sia, sehingga mengonsumsi listrik dalam jumlah besar. Akibatnya, PoW dianggap tidak ramah lingkungan dan kurang efisien, terutama ketika jaringan blockchain semakin besar dan tingkat kesulitannya terus meningkat.  
)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, sistem blockchain sederhana berhasil diimplementasikan dengan memanfaatkan fungsi hash SHA-256 dan mekanisme Proof of Work. Hasil pengujian menunjukkan bahwa setiap blok hanya dapat ditambahkan setelah memenuhi tingkat kesulitan tertentu, sehingga menjamin integritas dan keterkaitan antarblok. Dengan demikian, percobaan ini membuktikan bahwa blockchain mampu menjaga keamanan data transaksi melalui proses komputasi yang terverifikasi. )

---