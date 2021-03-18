## 1. Syntax Errors
Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian parsing,
mungkin merupakan jenis kesalahan paling umum yang dapatkan saat masih belajar Python.

## 2. Menangani Exceptions
Untuk memberitahu letak kesalahannya dimana dapat perintah try dan except.
Pernyataan try berfungsi sebagai berikut.

Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci try dan except) dieksekusi.

* Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: try selesai.

* Jika pengecualian terjadi selama eksekusi klausa try, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai dengan kata kunci exception, klausa except dioperasikan, dan kemudian eksekusi berlanjut setelah pernyataan try.

* Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke luar pernyataan try; jika tidak ada penangan yang ditemukan, ini adalah unhandled exception dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Klausa except yang berada di akhir dapat menghilangkan nama-(nama) exceptions, dan berfungsi sebagai wildcard.
Hati-hati ketika menggunakan wildcard ini, karena dapat menutupi kesalahan yang sebenarnya terjadi.

## 3. Memunculkan Exceptions
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi.

## 4. Pengecualian yang Ditentukan Pengguna
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru.
Pengecualian biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa saja yang dapat dilakukan oleh kelas lain, tetapi biasanya tetap sederhana,
seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan sebagai pengecualian.

## 5. Mendefinisikan Tindakan Pembersihan
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan.

Jika ada klausa finally, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk try selesai.
Klausa untuk finally dapat berjalan atau tidak apabila pernyataan try menghasilkan suatu pengecualian.
Poin-poin berikut membahas kasus yang lebih kompleks saat pengecualian terjadi:

* Jika pengecualian terjadi selama eksekusi klausa untuk :keyword: !try, maka pengecualian tersebut dapat ditangani oleh klausa except. Jika pengecualian tidak ditangani oleh klausa :keyword: !except, maka pengecualian dimunculkan kembali setelah klausa finally dieksekusi.

* Pengecualian dapat terjadi selama pelaksanaan klausa except atau else. Sekali lagi, pengecualian akan muncul kembali setelah klausa finally telah dieksekusi.

* Jika pernyataan klausa untuk try mencapai klausa break, continue atau :keyword:` return` maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.

* Jika klausa untuk :keyword:!finally` telah menyertakan pernyataan return, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan nilai dari try pernayataan untuk return.