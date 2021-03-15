## 1. Pemformatan Keluaran
Untuk menggunakan formatted string literals,
mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga.
Di dalam string ini, Anda bisa menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal.

## 2. Literal String Terformat
Formatted string literals (juga disebut f-string) memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {expression}.

## 3. Metode String format()
Jika tidak ada index pada tanda ‘{}’ maka tanda pertama dihitung sebagai index satu,
namun jika terdapat index maka format mengikuti index.

## 4. Pemformatan String Manual
Metode str.rjust() dari objek string merata-kanan-kan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri.
Ada metode serupa str.ljust() dan str.center().
Metode ini tidak menulis apa pun,
mereka hanya mengembalikan string baru. Jika string input terlalu panjang,
mereka tidak memotongnya,
tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda,
tetapi itu biasanya lebih baik daripada alternatif, yang akan berbohong tentang nilai.
(Jika Anda benar-benar menginginkan pemotongan, Anda selalu dapat menambahkan operasi slice, seperti pada x.ljust(n)[:n].)

## 5. Pemformatan string lama
Operator % (modulo) juga dapat digunakan untuk pemformatan string.
Diberikan 'string' % values, instansiasi dari % in string diganti dengan nol atau elemen yang lebih dari values.
Operasi ini umumnya dikenal sebagai interpolasi string.

## 6. Membaca dan Menulis Berkas
Argumen pertama adalah string yang berisi nama file.
Argumen kedua adalah string lain yang berisi beberapa karakter yang menggambarkan cara berkas akan digunakan.
mode dapat 'r' ketika file hanya akan dibaca, 'w' untuk hanya menulis (berkas yang ada dengan nama yang sama akan dihapus),
dan 'a' membuka berkas untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir.
'r+' membuka berkas untuk membaca dan menulis. Argumen mode adalah opsional; 'r' akan diasumsikan jika dihilangkan.

## 7. Menyimpan data terstruktur dengan json
Modul standar bernama json dapat mengambil hierarki data Python,
dan mengubahnya menjadi representasi string; proses ini disebut serializing.
Merekonstruksi data dari representasi string disebut deserializing.
Antara serializing dan deserializing, string yang mewakili objek mungkin telah disimpan dalam berkas atau data,
atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.