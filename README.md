Nama    : Akhyar Rasyid Asy syifa
NPM     : 2306241682
Kelas   : PBP - D

[ Link web: http://akhyar-rasyid-warunkchill.pbp.cs.ui.ac.id/ ]

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Jawab : 
    - [*Membuat Proyek Django*]
    Untuk membuat sebuah proyek Django baru, tentunya saya harus menyiapkan sebuah direktori baru terlebih dahulu. Direktori tersebut saya beri nama 'warunk_chill' sesuai dengan nama aplikasi yang akan saya buat. Lalu, saya harus menyiapkan dan menginstal beberapa depedencies yang ditambahkan ke berkas requirements.txt agar aplikasi yang saya buat dapat berfungsi. Tak lupa, saya menggunakan virtual environment untuk membantu mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang mungkin terdapat pada laptop saya.
    - [*Membuat Aplikasi main dalam direktori utama proyek*]
    Untuk membuat sebuah aplikasi main pada proyek 'warunk_chill' yang telah kita buat sebelumnya, kita dapat menjalankan perintah python manage.py startapp main untuk membuat sebuah struktur baru untuk aplikasi yang akan kita buat. Lalu, saya mendaftarkan aplikasi main ke dalam proyek warung-chill milik saya. Setelah itu, saya mengimplementasikan Template dan Model dasar untuk proyek aplikasi saya.
    - [*Melakukan routing pada proyek agar dapat menjalankan aplikasi main*]
    Untuk melakukan konfigurasi outing URL Aplikasi main, saya menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main milik saya. Lalu, saya mengimpor fungsi include dari django.urls untuk mengimpor rute URL dari aplikasi main ke dalam berkas urls.py proyek. Setelah itu, saya menambahkan rute Path URL 'main/' agar dapat diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main.
    - [*Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib*]
    Saya mengubah berkas models.py yang terdapat di dalam direktori aplikasi main untuk mendefinisikan model baru sesuai dengan yang diminta pada tugas. Untuk detailnya, model yang saya buat memiliki atribut name, price, dan description. Setiap atribut memiliki tipe data yang sesuai dengan yang diminta pada tugas seperti CharField, IntegerField, dan TextField.
    - [*Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML*]
    Untuk menghubungkan view dengan template, saya mengimpor fungsi render dari modul django.shortcuts untuk me-render tampilan HTML dengan menggunakan data yang diberikan. Setelah itu, saya mengubah template main.html agar dapat menampilkan data yang telah diambil dari model (agar dapat menampilkan nilai dari variabel yang telah didefinisikan dalam context).
    - [*Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py*]
    Untuk membuat sebuah routing pada urls.py aplikasi main, saya membuat berkas urls.py di dalam direktori main ntuk mengatur rute URL yang terkait dengan aplikasi main. Nantinya, fungsi show_main dari modul main.views akan dijadikan sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
    - [*Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat*]
    Untuk me-deploy ke Adaptable, saya memilih repositori proyek warunk_chill sebagai basis aplikasi yang akan di-deploy dan branch 'master' sebagai deployment branch. Karena dalam membuat proyeknya sebagian besar menggunakan bahasa Python, maka saya memilih Python App Template sebagai template deployment. Sebelum melakukan deployment, saya memasukkan nama aplikasi saya 'warunkchill' agar dapat digunakan juga sebagai nama domain situs web aplikasi saya.  Kemudian melakukan add, commit dan push perubahan yang terjadi pada direktori utama proyek. Setelah itu, melakukan deployment ke PWS membuat proyek baru kemudian nge git remote, add, dan push pws dari branch master. Terakhir setelah sudah di push menunggu beberapa menit untuk membuilding proyek di dalam Pacil Web Service dan kemudian proyek dapat dilihat dengan view project. Meski begitu, muncul log error saat building. Kemudian saya melakukan deploy kembali setelah saya menambahkan file Procfile untuk mengatasi error yang terjadi saat building di pws. Terakhir, saya mengulangi git remote, add, dan push ke pws lagi.

2. Alur sebuah request client ke web aplikasi berbasis Django beserta responnya menurut bagan tersebut adalah sebagai berikut:
![django concept](https://github.com/user-attachments/assets/aa57dc9a-f895-4e94-abcf-d18b40a71a9f)
    
    Pertama, request yang masuk ke dalam server Django akan diproses melalui urls.py untuk diteruskan ke views.py yang kita definisikan untuk memproses permintaan tersebut.
    Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya views.py akan memanggil query ke models.py dan database akan mengembalikan hasil dari query tersebut ke views.py.
    Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan pada template sebelum akhirnya HTML tersebut dikembalikan ke client sebagai respons.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    - Pelacakan Perubahan Kode: Git memungkinkan untuk melihat riwayat perubahan, siapa yang membuat perubahan, dan kapan perubahan itu terjadi
    - Manajemen Proyek dengan Repositori: Repositori digunakan sebagai tempat penyimpanan semua versi kode sumber beserta riwayat perubahannya.
    - Kloning Proyek: Pengembang dapat mengkloning proyek dan bekerja secara offline tanpa perlu selalu terhubung ke internet.
    - Branch : Git memungkinkan pengembang untuk membuat cabang yang berbeda guna mengerjakan bagian atau versi proyek tertentu
    - Merge : Perubahan yang dilakukan pada cabang dapat digabungkan kembali ke cabang utama setelah selesai.
    - Pull dan Push: Git memungkinkan pengembang untuk menarik (pull) versi terbaru dari repositori ke salinan lokal dan mendorong (push) perubahan dari lokal ke
      repositori utama.
    - Kolaborasi Pengembang: Git memfasilitasi kolaborasi banyak pengembang dalam proyek yang sama tanpa mengganggu pekerjaan satu sama lain.

4. Mengapa Framework Django Dipilih sebagai Permulaan Pembelajaran? 
    Jawab : Menurut saya, ketika seseorang baru mulai belajar bahasa pemrograman, python sering menjadi pilihan dasar karena kesederhanaannya. Seiring berjalannya waktu, saat ingin mempelajari pembuatan website, Django dianggap sebagai pilihan yang tepat karena dibangun menggunakan Python, sehingga lebih mudah dipahami oleh pemula dam sebagian besar pemula sudawh menguasai aspek fundamental python tersebut. Selain itu, Django juga memiliki dokumentasi yang sangat lengkap di internet, yang membuat proses pembelajaran lebih mudah ketika dihadapkan suatu masalah.

5. Mengapa Model pada Django Disebut sebagai ORM?
    Jawab : Model pada Django disebut sebagai ORM (Object Relational Mapper) karena Django mengkonversi objek Python menjadi query SQL untuk melakukan operasi database, tanpa harus menulis query SQL secara manual

