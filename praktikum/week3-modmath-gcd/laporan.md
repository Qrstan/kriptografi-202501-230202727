# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)  
Nama: Hartanti  
NIM: 230202727  
Kelas: 5IKRA  

---

Modular Arithmetic (Aritmetika Modular)
Modular arithmetic adalah sistem aritmetika untuk bilangan bulat yang "mengulang" setelah mencapai nilai tertentu (modulus). Seperti jam yang kembali ke 0 setelah 12, dalam modular arithmetic bilangan "berputar" kembali setelah mencapai modulus n. Ini adalah cabang teori bilangan yang mempelajari sisa pembagian dan sifat-sifatnya.
Definisi Dasar:
a ≡ b (mod n) berarti n membagi (a - b), atau sisa bagi a dan b terhadap n sama
Dibaca: "a kongruen dengan b modulo n"
n disebut modulus
Contoh: 17 ≡ 5 (mod 6) karena 17 - 5 = 12 habis dibagi 6, atau 17 dan 5 sama-sama bersisa 5 saat dibagi 6

Sifat-sifat Penting:
Penjumlahan: Jika a ≡ b (mod n) dan c ≡ d (mod n), maka:
(a + c) ≡ (b + d) (mod n)

Pengurangan:
(a - c) ≡ (b - d) (mod n)

Perkalian:
(a × c) ≡ (b × d) (mod n)

Perpangkatan:
a^k ≡ b^k (mod n)

GCD (Greatest Common Divisor / Faktor Persekutuan Terbesar)
GCD atau FPB (Faktor Persekutuan Terbesar) adalah bilangan bulat positif terbesar yang dapat membagi habis dua atau lebih bilangan sekaligus. GCD adalah konsep fundamental dalam teori bilangan yang mengukur "kesamaan" terbesar antara dua bilangan dalam hal faktor pembaginya.
Definisi Formal:
GCD(a, b) adalah bilangan bulat positif terbesar d sehingga:
d | a (d membagi a)
d | b (d membagi b)
Jika c | a dan c | b, maka c ≤ d

Algoritma Euclid:
Metode efisien mencari GCD berdasarkan prinsip bahwa GCD tidak berubah saat bilangan yang lebih besar diganti dengan sisa pembagiannya:
GCD(a, b) = GCD(b, a mod b)
GCD(a, 0) = a

Contoh:
GCD(48, 18):
48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0
Jadi GCD(48, 18) = 6
Cara Kerja: Algoritma berulang kali membagi bilangan yang lebih besar dengan yang lebih kecil, menggunakan sisa sebagai pembagi berikutnya, hingga sisa menjadi 0.

# Hasil pengujian dengan contoh kasus.
1. Modular Arithmetic (Aritmetika Modular)
Jam: 15:00 = 3:00 PM (15 ≡ 3 mod 12)
Hari dalam seminggu: 10 hari dari Senin = Kamis (10 ≡ 3 mod 7)

2. Membagi 48 apel dan 18 jeruk ke dalam paket yang sama besar tanpa sisa → maksimal 6 paket (GCD(48,18) = 6)
Dua roda gigi dengan 48 dan 18 gigi akan kembali ke posisi awal setelah LCM(48,18)/GCD(48,18) putaran

# Jawaban pertanyaan diskusi

1. Aritmetika modular memiliki peran penting dalam kriptografi modern karena menjadi dasar dari banyak algoritma keamanan, seperti RSA, Diffie-Hellman, dan ElGamal. Operasi dalam aritmetika modular memungkinkan perhitungan yang kompleks dilakukan dalam ruang bilangan terbatas, sehingga sulit untuk dibalik tanpa mengetahui kunci rahasia. Misalnya, proses enkripsi dan dekripsi pada RSA menggunakan perpangkatan modular, di mana hasil operasi tetap dalam batas modulus tertentu. Dengan sifatnya yang mendukung operasi satu arah namun sulit dibalik, aritmetika modular menjadi fondasi utama dalam menjaga kerahasiaan dan integritas data pada sistem kriptografi modern.

2. Invers modular penting dalam algoritma kunci publik seperti RSA karena digunakan untuk menghitung kunci dekripsi yang dapat membalik proses enkripsi. Dalam RSA, kunci publik digunakan untuk mengenkripsi pesan dengan operasi perpangkatan modular, sedangkan kunci privat dihitung sebagai invers modular dari eksponen publik terhadap fungsi totien modulus. Tanpa invers modular, proses dekripsi tidak dapat dilakukan karena tidak ada cara untuk membalik hasil enkripsi secara matematis. Dengan demikian, invers modular memastikan bahwa hanya pihak yang memiliki kunci privat yang dapat mengembalikan ciphertext menjadi plaintext secara aman.

3. Tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar adalah tingkat kesulitannya yang sangat tinggi secara komputasional. Ketika modulus bernilai besar, jumlah kemungkinan hasil menjadi sangat banyak, sehingga tidak ada cara efisien untuk menemukan eksponen yang sesuai selain mencoba satu per satu (brute force). Selain itu, meskipun ada algoritma yang lebih cepat seperti Baby-Step Giant-Step atau Pollard’s Rho, kompleksitasnya tetap meningkat secara eksponensial seiring ukuran modulus. Inilah sebabnya logaritma diskrit dianggap sebagai masalah yang sulit dan menjadi dasar keamanan berbagai sistem kriptografi modern seperti Diffie-Hellman dan ElGamal.