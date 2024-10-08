Nama    : Akhyar Rasyid Asy syifa <br>
NPM     : 2306241682 <br>
Kelas   : PBP - D <br>

WarunkChill🏪🥘🛒 <br>
"The Perfect Place to Chill and Fill." <br>
link APK : [WarunkChill](http://akhyar-rasyid-warunkchill.pbp.cs.ui.ac.id/)

### archive tugas🧑‍💻

<details>
<summary>📒 Tugas 2</summary>

## Tugas 2
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

## 2. Alur sebuah request client ke web aplikasi berbasis Django beserta responnya menurut bagan tersebut adalah sebagai berikut:
![django concept](https://github.com/user-attachments/assets/aa57dc9a-f895-4e94-abcf-d18b40a71a9f)
    
Pertama, request yang masuk ke dalam server Django akan diproses melalui urls.py untuk diteruskan ke views.py yang kita definisikan untuk memproses permintaan tersebut.
Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya views.py akan memanggil query ke models.py dan database akan mengembalikan hasil dari query tersebut ke views.py.
Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan pada template sebelum akhirnya HTML tersebut dikembalikan ke client sebagai respons.

## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Pelacakan Perubahan Kode: Git memungkinkan untuk melihat riwayat perubahan, siapa yang membuat perubahan, dan kapan perubahan itu terjadi
- Manajemen Proyek dengan Repositori: Repositori digunakan sebagai tempat penyimpanan semua versi kode sumber beserta riwayat perubahannya.
- Kloning Proyek: Pengembang dapat mengkloning proyek dan bekerja secara offline tanpa perlu selalu terhubung ke internet.
- Branch : Git memungkinkan pengembang untuk membuat cabang yang berbeda guna mengerjakan bagian atau versi proyek tertentu
- Merge : Perubahan yang dilakukan pada cabang dapat digabungkan kembali ke cabang utama setelah selesai.
- Pull dan Push: Git memungkinkan pengembang untuk menarik (pull) versi terbaru dari repositori ke salinan lokal dan mendorong (push) perubahan dari lokal ke
  repositori utama.
- Kolaborasi Pengembang: Git memfasilitasi kolaborasi banyak pengembang dalam proyek yang sama tanpa mengganggu pekerjaan satu sama lain.

## 4. Mengapa Framework Django Dipilih sebagai Permulaan Pembelajaran? 
Jawab : Menurut saya, ketika seseorang baru mulai belajar bahasa pemrograman, python sering menjadi pilihan dasar karena kesederhanaannya. Seiring berjalannya waktu, saat ingin mempelajari pembuatan website, Django dianggap sebagai pilihan yang tepat karena dibangun menggunakan Python, sehingga lebih mudah dipahami oleh pemula dam sebagian besar pemula sudawh menguasai aspek fundamental python tersebut. Selain itu, Django juga memiliki dokumentasi yang sangat lengkap di internet, yang membuat proses pembelajaran lebih mudah ketika dihadapkan suatu masalah.

## 5. Mengapa Model pada Django Disebut sebagai ORM?
Jawab : Model pada Django disebut sebagai ORM (Object Relational Mapper) karena Django mengkonversi objek Python menjadi query SQL untuk melakukan operasi database, tanpa harus menulis query SQL secara manual
</details>

<details>
<summary>📒 Tugas 3</summary>

## Tugas 3
## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengimplementasian sebuah platform, data delivery sangat diperlukan untuk proses pertukaran data antara satu bagian dengan bagian lainnya. lebih detailnya, alasan data delivery sangat diperlukan, yaitu : 
- Aksesibilitas: Menjamin ketersediaan data yang diperlukan untuk pengguna dan sistem melalui komunikasi antara frontend (yang digunakan oleh pengguna) dan backend (yang memproses data).
- Integrasi: Menyediakan kemampuan pertukaran data dengan sistem lain untuk keperluan integrasi antar platform atau aplikasi.
- Analisis real-time: Data delivery dapat mengupdate data dengan menyediakan data yang up-to-date untuk memastikan kebutuhan pengguna dengan mengambil keputusan yang cepat.
- Efisiensi: Mampu mempertahankan kecepatan dan skalabilitas platform melalui pengiriman data dengan volume yang besar secara efektif.
- Pengalaman Pengguna: Meningkatkan responsivitas dan kepuasan pengguna melalui pengiriman data yang cepat.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih unggul dibandingkan XML karena memiliki tingkat keterbacaan kode yang lebih baik. Struktur JSON yang menyerupai bentuk dictionary dalam Python, dengan konsep pasangan key:value, membuatnya lebih intuitif dan mudah dipahami oleh banyak pengembang. JSON lebih sering digunakan karena strukturnya yang ringkas dan sederhana, dibandingkan XML yang terlihat lebih rumit dan bertele-tele dalam penulisan. Ini mempermudah proses debugging dan pengembangan aplikasi.

Selain itu, integrasi JSON dengan bahasa JavaScript juga memberikan keuntungan besar, terutama dalam pengembangan aplikasi berbasis web. JSON sudah menjadi standar de facto dalam pertukaran data di lingkungan pengembangan modern karena kompatibilitasnya yang tinggi dengan banyak framework dan bahasa pemrograman. Kelebihan ini menjadikan JSON pilihan yang lebih efisien dan praktis untuk berbagai proyek dibandingkan XML, yang meskipun memiliki kelebihan seperti validasi melalui skema, sering kali dianggap kurang efisien dalam hal keringkasan dan kemudahan implementasi.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi kriteria validasi yang telah ditentukan di form fields, seperti `CharField`, `IntegerField`, `TextField`, dan lainnya. Method ini mengembalikan nilai boolean yang menunjukkan validitas data. Selain itu, `is_valid()` juga mengonversi inputan ke tipe Python yang sesuai, memastikan tidak ada karakter ilegal, dan mengatur data sesuai format yang diperlukan.

Kita memerlukan method ini untuk memastikan keamanan data dengan memvalidasi data sebelum dikirimkan ke database, sehingga mengurangi risiko adanya data berbahaya yang dapat menyebabkan error pada sisi server. Selain itu, method ini memberikan feedback yang jelas kepada pengguna atau pengembang mengenai kesalahan atau error yang terjadi pada input form data, sehingga memudahkan perbaikan dan penyesuaian.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token sangat penting dalam pembuatan form di Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). CSRF, atau yang sering disebut sebagai one-click attacks, adalah kerentanan keamanan di mana penyerang dapat mengirimkan permintaan berbahaya seolah-olah berasal dari pengguna yang sudah terautentikasi.

Jika suatu form tidak mengimplementasikan csrf_token, penyerang dapat dengan mudah melancarkan serangan CSRF. Platform akan menganggap setiap permintaan yang dilakukan adalah valid dan berasal dari pengguna yang sah. Dengan demikian, penyerang dapat mengirimkan permintaan berbahaya yang telah dirancang dengan baik untuk mengeksekusi tindakan yang tidak diinginkan.

Tanpa csrf_token, penyerang dapat memanfaatkan sesi yang sudah diautentikasi dan membuat permintaan jahat tanpa perlu mengetahui detail kredensial pengguna. Dengan kata lain, penyerang dapat meniru identitas pengguna dan membuat perubahan yang tidak diinginkan atau merugikan pada sistem, sehingga menimbulkan risiko keamanan yang signifikan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Membuat kerangka default pada views
- Membuat berkas html baru bernama base.html pada _root folder_ 
Sebelum membuat input form, karena halaman utama dan form memiliki beberapa bagian kode yang sama, saya membuat template umum untuk mengurangi pengulangan kode yang berulang. berikut isi `base.html`:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- lalu, agar `base.html` dapat digunakan, modifikasi lokasi folder `templates` ke `settings.py` dengan menambahkan
```
TEMPLATES = [
    {
        ... 
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```
- untuk meng-extend `base.html`, setiap berkas `.html`, dibaris paling atasnya ditambahkan dengan `{% extends 'base.html' %}`  
### 2. Pengimplementasian UUID
untuk mencegah terjadinya serangan IDOR pada proyek yang kita buat, perlu dilakukan pengubahan primary key dari models yang sebelumnya berbentuk integer menjadi UUID. Berikut hasil modifikasi saya:
```
from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Nama produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    description = models.TextField()  # Deskripsi produk
```
lakukan migrasi pada model tersebut.

### 3. Membuat forms.py di direktori main dengan isi :
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

### 4. Perbarui fungsi show_main, khususnya pada bagian context, agar dapat menghubungkan views.py dengan models.py 
```
def show_main(request):
    product_entries = Product.objects.all()

    context = {
        'app_name': 'warunk_chill',
        'name': 'Akhyar Rasyid Asy syifa',
        'class_name': 'PBP - D',
        'product_entries': product_entries
    }
    return render(request, 'main.html', context)
```

### 5. Membuat fungsi baru pada views.py
sebelum itu, `di views.py` saya melakukan import model dan form serta menambahkan mengimport redirect dari library `django.shortcuts.`

Selanjutnya di `views.py` juga, saya menambahkan fungsi baru bernama `create_product`. Berikut adalah potongan kode dari fungsi tersebut:
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
Secara general, fungsi tersebut akan menampilkan page create_product.html kepada user. Apabila form disubmit (request method POST) dan isinya valid (form.is_valid()), maka data yang diinput akan disimpan pada database dan fungsi akan melakukan redirect ke page utama.

### 6. Tambahkan berkas `create_product.html` pada direktori `main/templates/`
Berikut adalah isi dari `create_product.html`:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

### 7. Mengimplementasikan database ke dalam laman utama main.html dan juga menjadi perpanjangan dari base.html di direktori utama
tambahkan `main.html` dengan :
```
{% if not product_entries %}
<p>Belum ada data product pada Warunk Chill.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```

### 8. Routing URL ke laman yang bersangkutan di file `urls.py` di direktori main
```
urlpatterns = [
    ...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    ...
]
```

### 9. Membuat 4 fungsi yang diperlukan untuk menampilkan objek dengan XML, JSON, XML by ID, dan JSON by ID
untuk menampilkan data, baik secara keseluruhan ataupun berdasarkan hasil filtering UUID, dalam format XML, saya menambahkan views berikut dalam `views.py` yang terdapat pada direktori `main`.
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### 10. Merouting kembali URL yang bersangkutan di file `urls.py`
Untuk membuat routing URL dari masing-masing views tersebut, terlebih dahulu saya melakukan import views ke berkas `urls.py` di direktori `main/` dengan :
```from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id```
setelah melakukan import views, baru saya menambahkan path untuk routing url
```
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
Path pertama dan kedua digunakan untuk menampilkan seluruh data dalam format XML dan JSON. Sementara itu, path ketiga dan keempat berfungsi untuk menampilkan data yang difilter berdasarkan UUID, seperti yang terlihat pada bagian kode `<str:id>`. Jadi, jika kita ingin melihat produk dengan UUID tertentu dalam format JSON, kita cukup membuka URL `http://127.0.0.1:8000/json/<UUID>`.

### 11. Mengetest aplikasi pada localhost dengan command:
```python manage.py runserver```
kemudian membuka `http://localhost:8000/` di browser pilihan.

## Screenshot hasil akses URL pada postman
### - XML
<img width="1280" alt="bahan readme pbp 1" src="https://github.com/user-attachments/assets/acb7bd6f-3073-42af-9041-dc9a7c7dea4e">

### - JSON
<img width="1280" alt="bahan readme json" src="https://github.com/user-attachments/assets/4a4a74d4-a4a1-4a0b-a031-18d9d3aefac0">

### - XML by ID
<img width="1280" alt="bahan readme xml by id" src="https://github.com/user-attachments/assets/c94d0901-8ffc-4791-9588-d33abea9ddd0">

### - JSON by ID
<img width="1280" alt="bahan readme json by id" src="https://github.com/user-attachments/assets/229a2976-5587-484c-9e4e-da5f2d056d1e">
</details>

<details>
<summary>📒 Tugas 4</summary>

## Tugas 4
## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
-**`HttpResponseRedirect()`**:
`HttpResponseRedirect()` adalah kelas yang mengembalikan respons HTTP dengan status kode 302, yang memberitahu browser untuk mengarahkan ulang ke URL yang diberikan.
contoh penggunaan :
```
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some/url/')
```

-**`redirect()`**:
`redirect`adalah shortcut (fungsi pembantu) yang disediakan oleh Django untuk melakukan pengalihan. Method ini dapat menerima argumen berupa `model`, `views`, atau `url`. lalu, secara otomatis parameter ini akan dikonversi menjadi `url` dan menentukan path yang dituju.
contoh penggunaan :
```
from django.shortcuts import redirect

def my_view(request):
    return redirect('/some/url/')
```

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model `Product` dengan `User`, kita perlu menambahkan sebuah ForeignKey yang menghubungkan model `Product` dengan model `User`. `models.ForeignKey` sendiri berfungsi untuk menghubungkan product dengan satu `user` melalui sebuah relationship. Setiap objek `Product` akan memiliki seorang user yang bersifat One-to-Many (terlihat pada bagian ForeignKey), yaitu satu pengguna dapat memiliki lebih dari satu objek `Product`.  Contoh definisi model untuk menghubungkan `Product` dan `User` dapat dilihat dalam code berikut:
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # Nama produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    description = models.TextField()  # Deskripsi produk
```
lalu, terdapat penerapan `on_delete=models.CASCADE` yang berarti jika sebuah User dihapus, semua Product yang terhubung dengan User tersebut ikut dihapus.

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
_Authentication_ dan _authorization_ adalah dua konsep yang berbeda dalam keamanan komputer.
Untuk lebih detailnya, _authentication_ adalah proses untuk memverifikasi identitas pengguna. Hal ini dilakukan untuk memastikan bahwa pengguna yang mencoba mengakses sistem adalah pengguna yang sah. _Authentication_ dapat dilakukan dengan berbagai metode, seperti menggunakan nama pengguna dan kata sandi, menggunakan token keamanan, atau menggunakan biometrik.
Sedangkan, authorization adalah proses untuk menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu. Hal ini dilakukan untuk memastikan bahwa pengguna hanya dapat mengakses sumber daya yang mereka berhak akses. Authorization dapat dilakukan dengan berbagai metode, seperti menggunakan peran pengguna, menggunakan kebijakan akses, atau menggunakan kontrol akses berbasis objek. (Ibarat sebuah rumah, autentikasi adalah proses yang memverifikasi bahwa kita adalah pemilik rumah. Autorisasi adalah proses yang menentukan apakah kita memiliki izin untuk memasuki rumah tersebut.)
Keduanya memiliki beberapa perbedaan, yaitu:

-**`Authentication`**:
- Memverfikasi siapa pengguna sebenarnya
- Bekerja menggunakan kata sandi, OTP, informasi biometrik, dan informasi lain yang diberikan atau dimasukkan oleh pengguna
- Tahap pertama dalam proses pemeriksaan keamanan
- Terlihat dan sebagian dapat diubah oleh pengguna
- Django akan menggunakan `django.contrib.auth` untuk mengelola autentikasi pengguna dengan User sebagai model untuk menyimpan informasi pengguna.

-**`Authorization`**:
- Menentukan sumber daya apa yang dapat diakses pengguna
- Bekerja berdasarkan peraturan yang telah ditetapkan oleh developer atau organisasi pemilik aplikasi
- Selalu dijalankan setelah proses authentication selesai
- Tidak terlihat dan tidak dapat diubah oleh pengguna
- penggunaannya, perlu ditambahkan decorator seperti `@login_required` untuk memastikan bahwa hanya pengguna yang sudah login yang dapat mengakses view tertentu.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan memanfaatkan _session_ dan _cookies_. Setelah pengguna berhasil login, Django menghasilkan _session_ unik untuk pengguna tersebut dan menyimpannya di server. Selanjutnya, Django mengirimkan _session ID_ ke browser pengguna melalui cookies. Setiap kali pengguna mengirim permintaan ke server, browser akan menyertakan session ID tersebut, memungkinkan Django mengenali pengguna yang sedang login. Jika _session ID_ yang diterima sesuai dengan data sesi yang ada, Django dapat mengakses informasi pengguna terkait dan melanjutkan interaksi tanpa memerlukan pengguna untuk login lagi.

Cookies memiliki berbagai kegunaan lain, antara lain:
1. Menyimpan Data Login: Cookies dapat digunakan untuk menyimpan informasi login pengguna, sehingga mereka tidak perlu memasukkan kredensial setiap kali membuka aplikasi.
2. Pelacakan Aktivitas Pengguna: Situs web dapat menggunakan cookies untuk melacak aktivitas pengguna, seperti halaman yang sering dikunjungi atau item yang ditambahkan ke keranjang belanja.
3. Personalisasi Konten: Cookies memungkinkan situs web menyimpan preferensi pengguna, seperti tema, bahasa, atau pengaturan lainnya, sehingga pengalaman pengguna menjadi lebih personal.
4. Analitik dan Iklan: Cookies dapat digunakan untuk analisis lalu lintas situs web dan menampilkan iklan yang lebih relevan bagi pengguna berdasarkan aktivitas mereka.

"Apakah Semua Cookies Aman Digunakan?"
Tidak semua cookies aman digunakan. Ada beberapa risiko keamanan yang terkait dengan cookies, seperti _Hijacking_ , Serangan Cross-Site Scripting (XSS), dll. Hal ini karena cookies dapat disalahgunakan untuk menyimpan informasi sensitif seperti password atau data pribadi yang berisiko tinggi diambil oleh pihak yang tidak berwenang, misalnya hacker. Namun, django menyediakan beberapa flag bawaan yang dapat meminimalisir kemungkinan tersebut seperti Secure, HttpOnly, dan SameSite. Selain itu, cookies untuk sesi login perlu diatur masa berlakunya (_expiry_) untuk menghindari penyimpanan data yang tidak diperlukan terlalu lama.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Check 1 : Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

#### pengimplementasian ini diawali dengan menambahkan import dari django.contrib.auth.forms, django.contrib, dan django.contrib.auth pada `views.py` untuk kepentingan pembuatan form dan fungsi login dan logout yang akan saya buat.
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
```

#### Selanjutnya, saya membuat 3 fungsi utama, yakni register dengan implementasi `UserCreationFrom`, login dengan implementasi `AuthenticationForm`, dan logout
```
...
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
tambahan : 
-  saya menambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context` pada fungsi `show_main()`. Potongan kode tersebut-lah yang akan menampilkan kapan terakhir kali pengguna login. Tampilkan sesi terakhir login dengan menampilkan `last_login` di file `main.html`.

#### routing masing-masing fungsi tersebut (register, login dan logout) ke path yang terdapat dalam `main/urls.py`
```
urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

#### membuat 3 berkas HTML baru pada direktori main/templates sebagai template untuk pengembalian interface dari fungsi yang sebelumnya kita buat di views
- buat template `register.html` untuk menampilkan form register:
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

- buat template `login.html` untuk menampilkan form login:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

- untuk `logout`, Tambahkan link logout di template `main.html` untuk memudahkan pengguna keluar dengan :
```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

#### merestriksi halaman main
tambahkan import `login_required` pada `views.py` di `main`
```
from django.contrib.auth.decorators import login_required
```
dan juga `@login_required(login_url='/login')` di atas fungsi `show_main` di `views.py` agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
```
...
@login_required(login_url='/login')
def show_main(request):
...
```

### check 2 : Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Untuk membuat dua akun, kita bisa melakukan registrasi sebanyak dua kali dengan informasi yang berbeda untuk setiap akun. Langkah ini dapat dilakukan melalui form registrasi yang ada di aplikasi, di mana pengguna mengisi data yang diperlukan untuk membuat akun baru.

Selanjutnya, untuk membuat data dummy, kita perlu terlebih dahulu masuk (login) sebagai pengguna yang akan kita gunakan untuk menambahkan data dummy tersebut. Setelah berhasil login, kita dapat membuat beberapa data dummy baru dengan menggunakan form input yang sudah tersedia, misalnya melalui form POST yang telah kita buat sebelumnya pada Tugas 3. Data dummy ini dapat ditambahkan melalui tampilan aplikasi, di mana pengguna dapat mengisi informasi yang diinginkan dan mengirimkan data tersebut untuk disimpan dalam sistem.

Akun 1 dengan username user.akhyar
<img width="1280" alt="user 1" src="https://github.com/user-attachments/assets/3492a296-451a-46ae-ad16-ece90201e8f2">
<img width="226" alt="login user 1" src="https://github.com/user-attachments/assets/187b9338-fc5f-4d6e-9609-5bae4f106398">
<img width="323" alt="product 1 user 1" src="https://github.com/user-attachments/assets/ff7d075a-b01e-47a3-804e-8c81f4f4efa9">
<img width="314" alt="product 2 user 1" src="https://github.com/user-attachments/assets/399ec055-fe4c-4e8a-b20b-a4d42875bb38">
<img width="323" alt="product 3 user 1" src="https://github.com/user-attachments/assets/576acca5-68dc-4827-a3f4-6470c7cc682a">
<img width="1280" alt="hasil akhir user 1" src="https://github.com/user-attachments/assets/bea431f7-4d18-4c51-8272-68f738fc2691">

Akun 2 dengan username user.rasyid
<img width="1280" alt="user 2" src="https://github.com/user-attachments/assets/e0102cf9-6885-47f5-9b47-70e7e43efe84">
<img width="223" alt="login user 2" src="https://github.com/user-attachments/assets/d550feff-c988-4aff-beab-d4168dd99fca">
<img width="328" alt="product 1 user 2" src="https://github.com/user-attachments/assets/ff90bac5-fdf2-4a31-9ef4-0dd6037033a5">
<img width="324" alt="product 2 user 2" src="https://github.com/user-attachments/assets/fd8a4dd3-a967-4f36-be51-bc382457bfa4">
<img width="326" alt="product 3 user 2" src="https://github.com/user-attachments/assets/d91d7e91-49ba-4939-8c5c-06533f8e1031">
<img width="1280" alt="hasil akhir user 2" src="https://github.com/user-attachments/assets/96354286-8cf2-48aa-a0dd-daf427237fe9">


### check 3 : Menghubungkan model `product` dan `user`
#### Untuk menghubungkan model Product dengan User, saya perlu melakukan penambahan `ForeignKey` ke `user` di file main/models.py. 
```user = models.ForeignKey(User, on_delete=models.CASCADE)```

#### Kemudian, jangan lupa untuk melakukan migrate setelah perubahan pada models.py. Berikut commandnya :
```
python manage.py  makemigrations
python manage.py migrate
```
#### Mengubah fungsi `create_product` di `views.py`:
```
...
if form.is_valid() and request.method == "POST":
    product_entry = form.save(commit=False)
    product_entry.user = request.user
    product_entry.save()
    return redirect('main:show_main')
...
```
#### Kemudian, saya juga perlu melakukan sedikit perubahan pada fungsi show_main menjadi sebagai berikut :
```
@login_required(login_url='/login')
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)  # perubahan

    context = {
        'app_name': 'warunk_chill',
        'name': request.user.username,                           # perubahan
        'class_name': 'PBP - D',
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'main.html', context)
```

### check 4 : Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
#### Pada view `login_user`, dibuat supaya ketika seorang pengguna mencoba untuk log in dan berhasil, sebuah cookie dengan nama `last_login` akan dibuat dengan isi waktu saat pengguna login.
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now())) # set cookie disini
        return response
```
#### modifikasi show_main
Nama pengguna (username) dapat diakses dari objek request.user, yang menyimpan informasi tentang pengguna yang saat ini sedang login. Informasi cookies dapat ditemukan dalam dictionary request.COOKIES. Implementasi cookie berfungsi untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web.
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'warunk_chill',
        'name': request.user.username,
        'class_name': 'PBP - D',
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],  
    }
    return render(request, 'main.html', context)
```

#### modifikasi template 
Agar `last_login` ditampilkan maka saya perlu untuk melakukan penambahan kode di berkas `main.html`.
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

#### Langkah terakhir 
saya perlu mempersiapkan aplikasi ini untuk environment production. Untuk itu, saya perlu menambahkan kode pada direktori `warunk_chill/settings.py` dengan kode berikut :
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
</details>

<details>
<summary>📒 Tugas 5</summary>

## 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, berikut adalah urutan prioritasnya dari yang tertinggi hingga terendah:
  1. **inline styles** : Gaya yang ditulis langsung pada elemen HTML menggunakan atribut style memiliki prioritas tertinggi. contoh :
  ```<div style="color: red;">Hello</div>```
  2. **ID Selectors**: Selector yang menggunakan ID (diawali dengan `#`). Misalnya:
  ```#header { color: blue; }```
  3. **Class, Attribute, dan Pseudo-class Selectors**: Selector yang menggunakan class (.class), atribut ([attribute="value"]), dan pseudo-class (`:hover`, `:first-child`, dll). Contoh:
  ```.menu { color: green; }```
  4. **Element dan Pseudo-element Selectors**: Selector yang hanya menggunakan elemen (tag) HTML (div, p, span, dll) dan pseudo-element (`::before`, `::after`, dll). Misalnya:
  ```p { color: black; }```
  note : Important Rule (!important) dapat mengesampingkan semua urutan di atas dan memberikan prioritas tertinggi untuk suatu property.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Dengan desain yang responsif, pengalaman pengguna menjadi lebih baik karena mereka dapat mengakses konten dengan nyaman tanpa perlu melakukan zoom atau scroll berlebihan, sehingga meningkatkan kepuasan saat menggunakan aplikasi. Selain itu, responsive design memungkinkan aplikasi web menyesuaikan tampilannya untuk berbagai perangkat, seperti ponsel dan tablet, yang jumlah penggunanya terus meningkat. Hal ini memastikan aplikasi tetap terlihat baik dan mudah digunakan di berbagai ukuran layar, baik pada perangkat dengan layar kecil maupun besar.
- contoh aplikasi yang sudah menerapkan responsive design: amazon, adidas, youtube, tiktok, BBC News 
- contoh aplikasi yang belum menerapkan responsive design: SiakNG

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!


- 1. Padding : ruang di dalam elemen, antara konten dan batas (border) elemen tersebut. Padding meningkatkan jarak antara konten elemen dengan batas tepi elemen.
- 2. Border : garis yang mengelilingi elemen. Border berada di antara padding dan margin dan memberikan tampilan batas atau tepi pada elemen.
- 3. Margin : ruang di luar elemen yang mengatur jarak antara elemen tersebut dengan elemen lainnya. Margin mendorong elemen-elemen lain untuk menjauh.

##### contoh penerapan ketiganya : 
```
.box {
  padding: 15px;           /* Ruang di dalam elemen */
  border: 3px solid green;  /* Garis batas elemen */
  margin: 20px;            /* Ruang di luar elemen */
}
```

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid Layout adalah dua fitur CSS yang sangat powerful untuk mengatur tata letak elemen-elemen dalam sebuah halaman web.
#### Flexbox
**Konsep Dasar**: Flexbox dirancang untuk mengatur tata letak elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Bayangkan seperti sebuah kotak fleksibel yang berisi beberapa item. Kita dapat mengatur bagaimana item-item tersebut diatur di dalam kotak tersebut.
**Kegunaan**:
- Responsivitas: Sangat baik untuk membuat layout yang responsif, menyesuaikan diri dengan berbagai ukuran layar.
- Pengaturan Spasi: Dengan mudah mengatur jarak antara item, margin, padding, dan alignment.
- Distribusi Ruang: Memungkinkan kita untuk mendistribusikan ruang secara merata atau tidak merata di antara item-item.
- Order: Mengatur urutan tampilan item tanpa mengubah HTML.
- Basis untuk Layout Lebih Kompleks: Meskipun dirancang untuk satu dimensi, Flexbox sering digunakan sebagai dasar untuk membangun layout yang lebih kompleks.

#### Grid Layout
**Konsep Dasar**: Grid Layout memberikan cara yang lebih kuat untuk mengatur tata letak elemen dalam dua dimensi, seperti baris dan kolom. Bayangkan seperti sebuah tabel, tetapi dengan fleksibilitas yang jauh lebih tinggi.
Kegunaan:
- Layout Kompleks: Sangat cocok untuk membuat layout yang kompleks dengan banyak baris dan kolom.
Responsivitas: Mirip dengan Flexbox, Grid Layout juga sangat baik untuk membuat layout yang responsif.
- Template Grid: Mendefinisikan struktur grid yang kustom dengan baris dan kolom yang dapat disesuaikan.
- Area: Membagi grid menjadi area-area yang dapat diberi nama dan kemudian ditempatkan item ke dalamnya.
- Gaps: Menambahkan jarak antara baris dan kolom dengan mudah.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
### 1. checklist 1 :  Implementasikan fungsi untuk menghapus dan mengedit product.
##### Buat view untuk Edit dan Delete:
Untuk menambahkan fitur edit dan hapus produk dalam aplikasi, pertama-tama saya membuka file `views.py` dan membuat dua fungsi edit dan delete seperti berikut:
```
@login_required(login_url='/login')
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```

##### lalu saya membuat routing path di `urls.py` untuk edit dan delete
```
urlpatterns = [
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<str:id>', delete_product, name='delete_product'),
]
```

### checklist 2 : Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
#### Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
sebelum melangkah lebih jauh, saya menambahkan fitur CDN Styling supaya tidak perlu repot dalam mengkonfigurasi tailwind pada project
```
    <script src="https://cdn.tailwindcss.com">
    </script> 
```
letakkan di `base.html` di bawah `{% endblock meta %}`

###### lanjutkan kustomisasi `login.html`
- [Login Page](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/login.html)


###### lanjutkan kustomisasi `register.html`
- [Register Page](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/register.html)


###### lanjutkan kustomisasi `create_product_entry.html`
- [Create Product](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/create_product_entry.html)


###### lanjutkan kustomisasi `edit_product.html`
- [Edit Product](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/edit_product.html)


###### lanjutkan kustomisasi `main.html`
- [Daftar Product](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/main.html)


###### lanjutkan kustomisasi `product_card.html`
- [Card Product](https://github.com/akhyarrasyid/warunk-chill/blob/master/main/templates/product_card.html)


###### lanjutkan kustomisasi `navbar.html`
- [Navigation Bar](https://github.com/akhyarrasyid/warunk-chill/blob/master/templates/navbar.html)

</details>

## Tugas 6
## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memiliki banyak manfaat dalam pengembangan aplikasi web, salah satunya adalah memungkinkan kita untuk membuat halaman web yang lebih interaktif. Dengan JavaScript, kita dapat menambahkan fitur-fitur seperti animasi, validasi form, dan efek visual tanpa perlu melakukan refresh halaman. Hal ini tentu saja memberikan pengalaman yang lebih baik bagi pengguna.

Selain itu, JavaScript memungkinkan pengembangan aplikasi web yang lebih dinamis dan responsif, terutama melalui penggunaan teknologi seperti AJAX yang memungkinkan pengambilan data dari server tanpa perlu memuat ulang halaman. JavaScript juga mempermudah pengelolaan elemen-elemen pada halaman web secara langsung, sehingga kita bisa mengubah konten atau gaya tampilan secara real-time. JavaScript juga mendukung integrasi API, yang memudahkan kita dalam mengambil data dari sumber eksternal.

kalau membahas lebih jauh, framework dan library modern seperti React dan Vue.js dibangun di atas JavaScript, yang sangat membantu dalam membangun aplikasi web yang besar dan terstruktur. Selain itu, JavaScript tidak hanya terbatas pada browser, tetapi juga dapat digunakan di server dengan Node.js, sehingga memungkinkan pengembangan full-stack dengan satu bahasa pemrograman.

## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
await berfungsi untuk menunggu penyelesaian suatu proses asinkron, seperti fetch(), sebelum melanjutkan ke baris kode berikutnya. Dalam konteks fetch(), yang secara default mengembalikan Promise, penggunaan await memastikan bahwa kita menunggu hingga data dari server benar-benar diterima sebelum melanjutkan operasi lain, seperti pengolahan data.

Jika kita tidak menggunakan await, program akan langsung melanjutkan ke baris kode berikutnya tanpa menunggu hasil dari server, sehingga dapat menyebabkan kesalahan karena data mungkin belum tersedia saat kode mencoba mengaksesnya. Dengan menggunakan await, kita memastikan bahwa aplikasi berjalan sesuai urutan yang diharapkan, khususnya saat mengolah data dari server.

## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Django menerapkan perlindungan terhadap serangan Cross-Site Request Forgery (CSRF) untuk memastikan bahwa setiap permintaan POST yang dikirimkan ke server berasal dari sumber yang tepercaya. Django biasanya memeriksa token CSRF yang disertakan dalam setiap permintaan POST untuk mencegah serangan tersebut.

Namun, ketika kita menggunakan AJAX POST, mungkin token CSRF tidak disertakan dengan benar, yang menyebabkan permintaan POST ditolak oleh Django. Dalam kasus ini, kita dapat menggunakan decorator csrf_exempt pada view yang menangani AJAX POST untuk menonaktifkan pemeriksaan CSRF. Namun, kita perlu berhati-hati karena menonaktifkan CSRF dapat membuka potensi risiko keamanan.

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Meskipun pembersihan dan validasi data dapat dilakukan di frontend untuk meningkatkan pengalaman pengguna, validasi di backend tetap diperlukan untuk alasan keamanan. Pengguna dapat memanipulasi data yang dikirimkan ke server, misalnya dengan menggunakan developer tools atau alat lain untuk mengubah input setelah validasi di frontend dilakukan.

Karena itu, validasi di backend berfungsi sebagai lapisan pertahanan yang lebih kuat untuk memastikan bahwa data yang dikirimkan benar-benar sesuai dengan aturan yang telah ditetapkan dan tidak membahayakan sistem. Hal ini mencegah potensi serangan seperti SQL Injection atau Cross-Site Scripting (XSS), serta memastikan integritas data yang diterima oleh server. Dengan melakukan validasi di backend, kita memastikan bahwa input pengguna tetap aman meskipun validasi di frontend telah dilewati atau dimanipulasi.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### Pertama-tama, saya menambahkan pesan error pada view `login_user` seperti yang diajarkan pada tutorial.
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
else:
    messages.error(request, "Invalid username or password. Please try again.")
```
Walaupun langkah ini tidak disebutkan pada checklist, tetapi ini merupakan langkah pertama yang saya lakukan dalam mengerjakan tugas ini.

#### checklist 1 : Ubahlah kode cards data product agar dapat mendukung AJAX GET.
**note** : 
Untuk menambahkan kartu baru menggunakan AJAX GET dan POST, langkah awalnya adalah membuat fungsi JavaScript di dalam tag script pada `main.html`. Namun, berdasarkan referensi tutorial yang saya gunakan sebelumnya saat mengerjakan tugas, saya menerapkan AJAX POST terlebih dahulu untuk menambahkan kartu.
1. Untuk dapat menjalankan AJAX, hal pertama yang perlu dilakukan adalah dengan menambahkan sebuah fungsi `add_product_ajax` pada `views.py` agar dapat digunakan. Aktifkan decorator `@require_POST` dan `@csrf_exempt` untuk menunjang jalannya POST lewat AJAX.
```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("description")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")

    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        quantity=quantity,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```

2. Tambahkan method `strip_tags()` untuk memastikan data yang dikirim bebas dari semua tag HTML. Setelah itu, lakukan routing pada fungsi tersebut di `urls.py` agar bisa diakses dan terhubung dengan sistem.
```python
urlpatterns = [
...
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'))
]
```

3. saya perlu menghapus dua baris kode berikut pada fungsi `show_main` di berkasi `views.py` :
```python
...
products = Product.objects.filter(user=request.user)
...
'products': products,
...
```
4. Kemudian, saya perlu mengubah setiap baris pertama pada fungsi `show_json` dan `show_xml` pada berkas `views.py` menjadi kode berikut :
```python
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
5. Saya perlu menghapus kode dari blok condition `{% if not product_entries %}` hingga `{% endif %}` termasuk kondisinya dan merubahnya menjadi kode berikut :
```html
<div id="product_entry_cards"></div>
```

6. Lalu, saya perlu menambahkan tag script dan mengisinya dengan kode berikut untuk mendapatkan/get produk yang sudah terdaftar :
```html
<script>
  async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
</script>
```

#### Checklist 2 : Lakukan pengambilan data _product_ menggunakan AJAX `GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang _logged-in_.
7. Agar data produk dapat direfresh secara asinkronus serta menampilkan data dalam bentuk cards, maka saya perlu menambahkan baris kode berikut pada script :
```python
    async function refreshProductEntries() {
      // Kosongkan konten sebelumnya
      const productContainer = document.getElementById("product_entry_cards");
      productContainer.innerHTML = "";

      // Ambil data produk
      const productEntries = await getProductEntries();
      let htmlString = "";

      // Jika tidak ada produk, tampilkan gambar "sedih-banget"
      if (productEntries.length === 0) {
        htmlString = `
          <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-72 h-72"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data produk pada sistem.</p>
          </div>
        `;
      } else {
        // Tampilkan data produk dalam bentuk card
        productEntries.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const description = DOMPurify.sanitize(item.fields.description);
      
          htmlString += `
            <div class="bg-gray-300 rounded-lg p-3 min-w-[250px] max-w-md m-4">
              <h2 class="text-gray-700 font-bold text-xl mb-2">${item.fields.name}</h2>
              <p class="text-gray-700 mb-4">${item.fields.description}</p>
              <p class="text-gray-600 font-semibold">Price: Rp ${item.fields.price}</p>
              <p class="text-gray-600">Quantity: ${item.fields.quantity}</p>

              <!-- Tombol Edit dan Hapus -->
              <div class="flex justify-end space-x-2 mt-4">
                <a href="/edit/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                  </svg>
                </a>
                <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                </a>
              </div>
            </div>
          `;
        });
      }

      // Masukkan HTML produk ke dalam kontainer
      productContainer.innerHTML = htmlString;
    }
```

#### Checklist 3 : Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan _product_.
8. Saya perlu melakukan perubahan pada tombol add new product agar bisa membuka modal crud yang akan dibuat di step berikutnya. Hal ini demi memanfaatkan AJAX. Berikut kode setelah perubahan :
```python
<div class="flex justify-end px-6 mt-8 gap-x-4">
  <a href="{% url 'main:create_product_entry' %}">
    <button class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product Entry
    </button>
  </a>
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
    Add New Product Entry by AJAX
    </button>
</div>
```

#### Checklist 4 : Buatlah fungsi _view_ baru untuk menambahkan _product_ baru ke dalam basis data.
9. Agar fungsi penambahan produk dapat dijalankan, maka kita perlu membuat fungsi baru pada `views.py` (sudah disinggung di langkah nomor 1 sebenarnya) dengan menambahkan kode sebagai berikut :
```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("description")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")

    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        quantity=quantity,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```

#### Checklist 5 : Buatlah fungsi _view_ baru untuk menambahkan _product_ baru ke dalam basis data.
10. sudah disinggung di langkah nomor 2
```python
urlpatterns = [
...
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'))
]
```

#### Checklist 6 : Hubungkan form yang telah kamu buat di dalam modal kamu ke _path_  `/create-ajax/`.
11. Saya perlu membuat modal yang digunakan untuk form penamabahan produk baru. Hal itu dapat dilakukan dengan melakukan penambahan kode berikut di `main.html` :
```html
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
      <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
          <h3 class="text-xl font-semibold text-gray-900">
            Add New Mood Entry
          </h3>
          <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>

        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style">
          <form id="productEntryForm">
            <div class="mb-4">
              <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
              <input type="text" id="name" name="name" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your product name" required>
            </div>
            <div class="mb-4">
              <label for="description" class="block text-sm font-medium text-gray-700">Product Description</label>
              <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe your product(s)" required></textarea>
            </div>
            <div class="mb-4">
              <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
              <input type="number" id="price" name="price" min="1" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" required placeholder="Enter the product's price">
            </div>
            <div class="mb-4">
              <label for="quantity" class="block text-sm font-medium text-gray-700">Quantity</label>
              <input type="number" id="quantity" name="quantity" min="1" class="mt-1 block w-full border text-black border-gray-300 rounded-md p-2 hover:border-indigo-700" required placeholder="Enter the quantity">
            </div>
          </form>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
          <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
          <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
      </div>
    </div>
```

12. Agar modal form tersebut dapat berjalan sebagaimana mestinya, maka saya perlu menambahkan baris script baru sebagai berikut :
```html
<script>
  ...
  // Tambahkan event listener untuk tombol "Add New Product Entry"
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
...
</script>
```

13. Agar form pada crud model dapat melakukan submit dan menambahkan produk sesuai input pengguna pada database, maka saya perlu menambahkan baris kode berikut pada tag `<script>`:
```html
<script>
  ...
  function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())
    
    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();
    
    return false;
  }
  ...
</script>
```

14. Untuk meminimalisir serangan _Cross Site Scripting_, maka saya perlu melakukan beberapa perubahan pada kode saya. Pertama, saya perlu menambahkan baris kode berikut pada `views.py` dan sudah dibahas pada nomor 1 dan 2 yaitu menambahkan `strip_tags`
```python
...
from django.utils.html import strip_tags
...
@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name")) # sudah ada pada kode sebelumnya
    description = strip_tags(request.POST.get("description")) # sudah ada pada kode sebelumnya
    ...
```

Saya juga perlu melakukan hal yang sama pada `forms.py`. Berikut penambahan kodenya :
```python
...
from django.utils.html import strip_tags
...
class  ProductForm(ModelForm):
...
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
```

15. Saya juga perlu membersihkan data yang sudah terlanjur terdaftar. Untuk melakukan hal itu, saya menggunakan DOMPurify. Pada `main.html`, saya perlu mengimport script baru sebelum end block meta. Berikut penambahan kodenya :
```html
{% block meta %}
...
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
...
{% endblock meta %}
```

16. YEAYY SELESAI. Warunk Chill sudah siap sedia menerima pesananmu.