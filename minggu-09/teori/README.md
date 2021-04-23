# Virtual Environment dan Package Manager

## Menciptakan Lingkungan Virtual
Untuk membuat lingkungan virtual, tentukan direktori tempat Anda ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori.

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan membuat Anda mendapatkan versi dan instalasi Python tertentu. Sebagai contoh:

## Mengelola Paket dengan pip
Anda dapat menginstal versi terbaru dari suatu paket dengan menyebutkan nama suatu paket.

Anda juga dapat menginstal versi spesifik suatu paket dengan memberikan nama paket diikuti dengan == dan nomor versi.
 
pip show akan menampilkan informasi tentang paket tertentu.

pip list akan menampilkan semua paket yang diinstal di lingkungan virtual.
 
pip freeze akan menghasilkan daftar yang sama dari paket yang diinstal, tetapi keluarannya menggunakan format yang diharapkan oleh pip install. Sebuah konvensi yang umum digunakan adalah meletakkan daftar ini dalam file requirements.txt:
 
requirements.txt kemudian dapat dikirimkan atau commit ke sistem kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan install -r:
 
# Getting Started with Conda

Perintah - perintah conda:

1. ```conda --version``` Mengecek versi conda.

2. ```conda update conda``` Mengupdate versi conda menjadi yang terbaru.

3. ```conda create --name snowflakes biopython``` Membuat lingkungan baru dengan nama snowflakes dan menginstall paket biopython.

4. ```conda activate snowflakes``` Mengaktifkan lingkungan snowflakes.

5. ```conda info --envs``` Melihat semua lingkungan yang ada pada conda.

6. ```conda activate``` Mengembalikan lingkungan ke lingkungan default.

7. ```conda create --name snakes python=3.5``` Membuat lingkungan baru dengan nama snakes dan menggunakan versi python 3.5 pada lingkungan tersebut.

8. ```conda search beautifulsoup4``` Memeriksa apakah paket yang belum terinstal dengan bernama "beautifulsoup4" tersedia dari repository Anaconda.

9. ```conda install beautifulsoup4``` Menginstal paket ini ke lingkungan saat ini.

10. ```conda list``` Memeriksa apakah paket yang baru diinstal ada di lingkungan ini.