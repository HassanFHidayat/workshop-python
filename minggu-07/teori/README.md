## 1. Classes
Classes atau kelas-kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru menghasilkan objek dengan type baru, memungkinkan dibuat instance baru dari tipe itu. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari sebuah class juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.

## 2. Lingkup Python dan Namespaces
Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan.
Suatu scope adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Directly accessible" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di namespace.

## 3. Kelas
Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. (Anda dapat menempatkan definisi kelas di cabang dari pernyataan if, atau di dalam suatu fungsi.)
Dalam praktiknya, pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi pernyataan lain diizinkan, dan terkadang berguna. Definisi fungsi di dalam kelas biasanya memiliki bentuk khusus daftar argumen, didikte oleh konvensi pemanggilan untuk metode.

## 4. Objek Instance
data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan.

## 5. Variabel Kelas dan Instance
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas.

## 6. Pewarisan
Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Python mendukung bentuk pewarisan berganda juga.

## 7. Iterators
Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas. Definisikan metode __iter__() yang mengembalikan objek dengan metode __next__(). Jika kelas mendefinisikan __next__(), maka __iter__() bisa langsung mengembalikan self.

## 8. Pembangkit Generator
Generators adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi. Generators adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi.

## 9. Ekspresi Pembangkit Generator
Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku.