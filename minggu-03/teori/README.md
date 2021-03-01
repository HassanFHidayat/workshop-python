** 1.	List
list.append(x),	untuk menambahkan item pada akhir list.
list.extend(itterable),	memperluas list dengan menambahkan semua item dari iterable.
list.insert(i,x),	memasukkan item pada posisi tertentu
list.remove(x),	menghapus item yang ditunjuk x.
list.pop([i]),	hapus item pada posisi yang diberikan dalam daftar, dan kembalikan
list.clear(),	hapus semua item dari daftar list
list.index(x[, start[, end]]), mencari posisi suatu nilai
list.count(x), menghitung kemunculan nilai tertentu
list.sort(*, key=None, reverse=False), mengurutkan list
list.reverse(), balikkan elemen daftar list di tempatnya
list.copy(), kembalikan salinan daftar list yang terdekat

*** Stack
Metode list memudahkan untuk menggunakan list sebagai stacks, 
dimana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil.
Metode append() digunakan untuk menambhkan item ke dalam stack. Metode pop() digunakan untuk mengambil item dari atas stack.
 
 

*** Queue
Queue juga dapat dibuat menggunakan list,
di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil.
Namun, list tidak efisien untuk tujuan ini.
Implementasi yang digunakan adalah menggunakan metode collections.deque.

*** List Comprehensions
Penggunaan list paling umum adalah membuat list, 
di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau dapat diulang.

*** Nested List
Ekspresi awal dalam pemahaman list dapat berupa ekspresi sembarang apa
pun, termasuk pemahaman list lainnya.

** 2.	del statement
Ada cara untuk menghapus item dari list yang diberikan indeksnya,
del juga dapat digunakan untuk menghapus irisan dari list atau menghapus seluruh list

** 3.	Tuples dan Sequences
Tupel adlaah tipe data urutan standar lain dalam Python.
Tupel terdiri dari sejumlah nilai yang dipisahkan dengan koma.

** 4.	Sets
Satu set adalah koleksi tidak berurutan tanpa elemen duplikat.
Set objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.
Tanda kurung kurawal atau set() fungsinya dapat digunakan untuk membuat set.

** 5.	Dictionary
Kamus terkadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "larik asosiatif".
Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. 

** 6.	Looping Techniques
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().
 
Saat mengulang melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi enumerate().
 
Untuk mengulang dua urutan atau lebih secara bersamaan, entri dapat dipasangkan dengan fungsi zip().
 
Untuk mengulangi sebuah urutan sequence dalam susunan yang diurutkan,
gunakan fungsi sort() yang mengembalikan daftar terurut baru dengan membiarkan sumber tidak diubah.
 

 

** 7.	More on Conditions
Perhatikan bahwa dalam Python, tidak seperti C, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus :=.
Ini menghindari masalah kelas umum yang dihadapi dalam program C: mengetikkan = dalam ekspresi ketika == dimaksudkan.
 
