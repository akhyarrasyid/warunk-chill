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


### - JSON


### - XML by ID


### - JSON by ID

