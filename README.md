Nama : Rebeccaniaga Napitupulu
NPM : 2506598394
Kelas : PBP E
Dosen : Pak Daya

Live demo: https://rebeccaniaga-napitupulu-myportofolio.pws.cs.ui.ac.id

# Tentang Proyek : 
Proyek ini merupakan Tugas Individu mata kuliah Pemrograman Berbasis Platform (PBP), yang melanjutkan langsung dari Tutorial. Halaman ini berisi:
- Home (Hero Section) : perkenalan singkat, foto profil, dan tautan media sosial.
- About Me : enam karakteristik personal yang menggambarkan diri saya, ditampilkan dalam layout grid dengan efek hover.
- Education : timeline riwayat pendidikan dari SD hingga perkuliahan saat ini, ditampilkan dalam bentuk garis waktu zig-zag yang responsif.
- Experience : daftar pengalaman organisasi / internship, ditampilkan dalam bentuk kartu berdasarkan data dari database (model Django).

# Tech Stack:
- Django (struktur proyek, template rendering, static files)
- HTML5 (elemen semantik: <header>, <section>)
- CSS3 murni (custom properties, Flexbox, Grid, media query tanpa framework CSS)
- Lucide Icons (untuk ikon generik) & SVG inline custom (untuk ikon brand GitHub/LinkedIn/Instagram)
- Deployment: PWS (Pacil Web Service)

# Cara Menjalankan Proyek Secara Lokal
# 1. Clone repository
git clone https://pws.cs.ui.ac.id/rebeccaniaga.napitupulu/myportofolio
cd myportofolio

# 2. Buat dan aktifkan virtual environment
python -m venv env
env\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan development server
python manage.py runserver

# Progress Minggu 1 :
- Membangun halaman "About Me" dasar sesuai Tutorial 01 dengan data placeholder.
- Mengisi ulang seluruh konten dengan data pribadi asli (nama, NPM, foto, bio).
- Merancang ulang tampilan menjadi tema dark purple & amber, menggantikan seluruh class Tailwind menjadi CSS murni yang ditulis manual di style.css.
- Menambahkan section baru Education berupa timeline riwayat pendidikan dengan layout zig-zag di desktop dan satu kolom di mobile.
- Memperbaiki bug ikon media sosial (GitHub, LinkedIn, Instagram) yang tidak muncul karena pustaka Lucide tidak lagi menyediakan ikon brand tersebut diganti dengan SVG custom.
- Mengonfigurasi pemanggilan file statis (CSS, gambar, PDF CV) menggunakan {% load static %} dan {% static %} agar dapat terbaca oleh Django.
- Deploy proyek ke PWS dan menyelesaikan konflik merge antara commit lokal dengan commit awal dari server.

### Tugas 1

1. # Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Saya menggunakan elemen semantik HTML5 dalam merancang struktur halaman portofolio saya. Saya memakai elemen <header> untuk bagian navbar, serta elemen <section> untuk membagi halaman menjadi beberapa bagian utama, yaitu <section id="home"> untuk bagian hero, <section id="about"> untuk bagian perkenalan diri, dan <section id="education"> untuk bagian riwayat pendidikan yang saya tambahkan sebagai section baru.

Penggunaan elemen semantik ini sangat membantu saya, terutama ketika saya sedang menyusun ulang kode dari struktur berbasis Tailwind menjadi CSS murni. Karena setiap section memiliki identitas (id) yang jelas, saya dapat dengan mudah menelusuri bagian mana yang sedang saya edit tanpa harus membaca ulang keseluruhan kode dari awal. Selain itu, id pada tiap section juga saya hubungkan dengan menu navigasi, sehingga ketika pengguna mengklik menu tersebut, halaman akan otomatis melakukan scroll menuju bagian yang dituju. Apabila saya hanya menggunakan elemen <div> tanpa struktur semantik yang jelas, proses pengelolaan dan pengembangan halaman akan menjadi lebih sulit dan membingungkan.

Saya belum menggunakan elemen <article> maupun <aside> karena konten yang saya buat masih saling berkaitan erat dengan section induknya dan belum memerlukan pemisahan lebih lanjut sebagai konten yang berdiri sendiri.

2. # Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Tantangan responsive yang paling saya rasakan muncul saat saya mengubah struktur layout dari berbasis Tailwind menjadi CSS manual. Tantangan terbesar terletak pada bagian timeline Education. Pada tampilan desktop, kartu timeline ditampilkan secara zig-zag bergantian kiri dan kanan dari garis tengah. Namun ketika ditampilkan pada layar kecil, tata letak tersebut menjadi tidak rapi apabila tetap dipaksakan dalam bentuk zig-zag. Oleh karena itu saya menggunakan breakpoint @media (min-width: 768px) agar tampilan zig-zag hanya diterapkan pada layar desktop, sedangkan pada tampilan mobile seluruh kartu ditampilkan sejajar dalam satu kolom.

Selain itu, menu navigasi pada bagian tengah header juga menjadi tantangan tersendiri. Ketika ditampilkan pada layar ponsel, menu tersebut menjadi terlalu sempit dan tidak proporsional, sehingga saya memutuskan untuk menyembunyikan menu tersebut pada tampilan mobile dan hanya menyisakan logo serta tombol Hire Me.

Dalam mengevaluasi elemen mana yang perlu diprioritaskan, saya mempertimbangkan elemen apa yang paling penting untuk dilihat terlebih dahulu oleh pengunjung pada layar kecil. Saya menyimpulkan bahwa foto dan nama merupakan elemen utama yang harus tetap jelas dan tidak berubah posisi secara drastis, sementara elemen dekoratif seperti badge kecil maupun efek visual lainnya dapat menyesuaikan secara otomatis.

3. # Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Batasan utama yang saya rasakan adalah seluruh konten harus ditulis manual di dalam HTML. Sebagai contoh, saat mengganti ikon media sosial, saya harus mencari dan menambahkan kode SVG satu per satu karena pustaka ikon yang saya pakai sudah tidak menyediakan ikon brand tersebut. Saya juga sempat kesulitan saat berpindah ke Django, karena path pemanggilan berkas statis (CSS, gambar, PDF) yang sebelumnya berfungsi ternyata tidak terbaca dan harus diganti menggunakan {% static %}. Selain itu, halaman ini juga belum memiliki interaksi nyata dengan pengunjung, misalnya tombol Download CV yang hanya berupa tautan statis tanpa fitur tambahan apa pun.

Berdasarkan batasan tersebut, pada iterasi selanjutnya menggunakan arsitektur MVT di Django, saya ingin menyimpan data Education dan Projects dalam bentuk model basis data agar dapat dikelola melalui admin panel tanpa mengubah kode HTML, serta menambahkan formulir kontak sederhana agar pengunjung dapat mengirim pesan langsung dari halaman portofolio.

AI Disclosure Tugas 1 :Saya menggunakan bantuan AI (Chatgpt) untuk konversi Tailwind ke CSS murni, penyusunan section baru, dan debugging saat deployment ke PWS. Beberapa keterbatasan yang saya temukan dan perbaikan manual yang saya lakukan: pertama, AI membantu menerjemahkan class utility Tailwind menjadi CSS custom, namun saya tetap perlu memverifikasi ulang nilai padding, warna, dan breakpoint responsive secara manual agar sesuai tampilan aslinya. Kedua, AI awalnya menyarankan pustaka Lucide untuk seluruh ikon, tetapi ikon GitHub, LinkedIn, dan Instagram tidak muncul karena versi terbaru Lucide sudah tidak menyediakan ikon brand, sehingga saya meminta solusi alternatif dan menerapkan SVG inline sebagai gantinya lalu memverifikasinya manual di browser. Ketiga, path CSS, gambar, dan CV yang sebelumnya berfungsi ternyata tidak terbaca saat dijalankan lewat Django; AI menjelaskan penggunaan {% load static %} dan {% static %}, yang kemudian saya terapkan dan uji manual satu per satu. Secara umum, AI mempercepat proses penulisan kode dan penjelasan konsep, tetapi saya tetap melakukan verifikasi dan perbaikan manual pada bagian yang berkaitan dengan pustaka pihak ketiga yang sudah usang dan perbedaan lingkungan antara HTML statis biasa dengan proyek Django.

Sumber : https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section

# Progress Minggu 2 :
- Menambahkan model Education dan AboutTrait pada aplikasi main, masing-masing dengan field yang merepresentasikan data riwayat pendidikan dan karakteristik personal.
- Membuat dan menerapkan migrasi untuk kedua model tersebut.
- Membuat view show_education dan show_about yang mengambil data dari model dan meneruskannya ke template melalui context.
- Mengonversi halaman Education dan About dari konten hardcoded menjadi halaman dinamis menggunakan perulangan Django Template Language ({% for %}), lengkap dengan kondisi tampilan kosong ({% empty %}).
- Mendaftarkan named route baru (show_education, show_about) pada main/urls.py dan menghubungkannya ke navbar menggunakan tag {% url %}.
- Memperbaiki inkonsistensi navbar di beberapa halaman (Education dan Experience) yang masih mengarah ke anchor link lama (#about, #education) alih-alih halaman baru yang sudah terpisah.
- Menambahkan hamburger menu untuk navigasi pada tampilan mobile beserta CSS dan JavaScript pendukungnya.
- Menulis unit test untuk halaman Education, About, dan Experience, masing-masing mencakup pengujian akses URL dan template, kemunculan data ketika ada, dan pesan kondisi kosong ketika tidak ada data. Seluruh 12 test berhasil lulus.

### Tugas 2
1. # Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

Jadi alurnya kira-kira begini waktu user ketik URL atau klik navbar (misalnya /education/), request itu pertama kali sampai ke urls.py di level proyek (folder yang sama dengan settings.py). Di situ Django cuma ngecek prefix pathnya, terus kalau cocok dia lempar ke urls.py punya aplikasi main lewat include(). Nah di urls.py aplikasi ini baru dicocokkan lagi path spesifiknya (misal education/) sama function view yang sesuai, contohnya show_education. View ini kerjanya manggil data dari model, di kasusku Education.objects.all(), jadi dia ambil semua baris data pendidikan yang ada di database. Data itu terus dimasukin ke dictionary context, lalu dikirim ke template pakai render(). Template education.html ini isinya loop {% for item in education_list %} yang bakal otomatis generate HTML sesuai jumlah data yang ada, tanpa perlu ditulis manual satu-satu. Terakhir hasil HTML jadi itu dikirim balik sebagai response ke browser dan ditampilkan ke user.

2. # Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Karena kalau datanya ditulis langsung di template, itu sama aja kayak ngehardcode, jadi setiap kali ada perubahan (misal nambah riwayat pendidikan baru atau ganti deskripsi), aku harus buka dan edit file HTMLnya langsung. Itu ribet dan gampang salah, apalagi kalau data yang sama ternyata dipakai di lebih dari satu tempat. Dengan disimpen di model/database, aku cukup nambah data lewat shell, dan tampilannya otomatis update tanpa perlu sentuh kode HTML sama sekali. Ini juga bikin templatenya jadi lebih fokus cuma ngurusin tampilan aja (presentation), sementara logic dan data terpisah di model, jadi kalau nanti mau develop fitur baru atau ada bug, aku tahu persis harus cek di bagian mana.

3. # Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

makemigrations itu fungsinya bikin "rencana perubahan" berupa file migrasi berdasarkan perubahan yang aku buat di models.py, tapi belum benar-benar mengubah apapun di database. Sedangkan migrate itu yang benar-benar mengeksekusi rencana tadi ke database beneran, jadi tabel dan kolomnya baru keupdate di situ. Contoh kasusnya waktu aku bikin model Education, aku nambahin field kayak tags dan color_theme. Setelah nulis field itu di models.py, aku jalanin makemigrations dulu supaya Django bikin file migrasi yang isinya instruksi "tambah kolom tags dan color_theme ke tabel Education", baru habis itu aku jalanin migrate biar instruksi itu beneran dieksekusi dan kolom-kolom itu muncul di database.

AI Disclosure Tugas 2: Dalam implementasi MVT (Education, About, Experience), saya menggunakan AI sebagai bantuan untuk memahami konsep MVT dan mengetahui hubungan antara Model, View, dan Template dalam Django. AI juga membantu menjelaskan bagian kode yang perlu dibuat atau diubah, memberikan contoh struktur kode seperti model, view, URL, template, serta unit test, sehingga saya lebih mudah memahami cara mengimplementasikan konsep tersebut ke dalam tugas. Setelah mendapatkan penjelasan dan contoh dari AI, saya tetap menyesuaikan kode dengan struktur project yang saya gunakan dan melakukan pengecekan secara mandiri.

Beberapa hal yang saya temukan perlu diperbaiki sendiri adalah, pertama, AI sempat memberikan contoh nama URL seperti show_main dan show_experience tanpa menyesuaikannya dengan namespace main yang saya gunakan di urls.py. Ketika dicoba, kode tersebut menghasilkan error sehingga saya mengecek kembali konfigurasi URL dan menyesuaikannya secara manual menjadi {% url 'main:show_education' %} dan URL lainnya sesuai dengan app_name yang digunakan. Kedua, saat membuat navbar yang konsisten di empat halaman berbeda, yaitu home, about, education, dan experience, saya sempat menggunakan kembali navbar lama yang masih menggunakan anchor link seperti #about dan #education. Karena halaman sudah dipisahkan, beberapa link menjadi tidak sesuai. Saya mengecek setiap halaman secara manual dan memperbaikinya agar menggunakan {% url %} yang mengarah ke halaman masing-masing. Ketiga, saat membuat hamburger menu untuk tampilan mobile, menu sempat tidak muncul di local karena perubahan CSS belum terupdate dan terdapat typo kecil pada HTML, yaitu class="main-nav"id="mainNav" yang tidak memiliki spasi. Saya menemukan dan memperbaiki bagian tersebut secara manual setelah melakukan pengecekan terhadap kode dan hasil tampilan di local.

Sumber : https://www.freecodecamp.org/news/how-django-mvt-architecture-works/

# Progress Minggu 3 :
- Menambahkan model Experience dengan beberapa field bertipe beda-beda: title (CharField), description (TextField), category (CharField dengan choices), thumbnail (URLField), sama ended_at (DateTimeField, opsional buat nandain masih berlangsung atau sudah selesai).
- Membuat ExperienceForm di forms.py pake ModelForm, isinya semua field yang bisa diisi user (title, description, category, thumbnail, ended_at), kecuali id sama started_at yang emang auto-generate.
- Membuat fungsi view buat create (create_experience), update (edit_experience), delete (delete_experience), dan ngambil data dalam bentuk JSON (get_experience_json) pake serializers.serialize.
- Membuat halaman form yang sama dipake buat create dan edit (experience_form.html), jadi nggak perlu duplikat template.
- Menampilkan data experience di experience.html pake perulangan {% for %}, lengkap sama tombol Edit dan Hapus yang connect ke masing-masing view di atas.
- Refactor beberapa halaman (experience.html, project.html, dll) biar semua extend dari base.html, jadi navbar, header, sama footer nggak perlu ditulis ulang di tiap halaman.

### Tugas 3
1. # Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

Jadi kalau bikin form HTML manual, aku harus menulis sendiri semua fieldnya satu-satu, plus validasinya juga harus aku handle sendiri di view (misal ngecek apakah titlenya kosong, apakah urlnya valid, dsb). Sedikit ribet dan rawan salah, apalagi kalau modelnya udah aku definisiin duluan di models.py jadinya seperti nulis dua kali hal yang sama. Nah, ModelForm ini ngambil alih kerjaan itu, dia otomatis generate field form berdasarkan field yang ada di model, lengkap sama validasinya juga (misal thumbnail yang URLField otomatis divalidasi harus berupa URL yang valid). Jadi aku tinggal define Meta.fields aja, terus tinggal panggil form.save() buat langsung simpan ke database, tidak perlu nulis query manual.

Soal {% csrf_token %}, itu wajib ada di form yang methodnya POST karena buat mencegah serangan CSRF (Cross-Site Request Forgery), yaitu situs jahat yang nyoba ngetrigger form submit ke situs kita pake identitas user yang lagi login, tanpa user itu sadar. Token ini digenerate unik tiap request sama Django, terus dicocokin lagi pas form disubmit. Kalau tokennya nggak ada atau nggak cocok, Django bakal nolak requestnya (403 Forbidden). Jadi ini basically lapisan keamanan biar form cuma bisa disubmit dari halaman yang emang dirender sama server sendiri.

2. # Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
Menurutku alasan utamanya karena JSON jauh lebih ringkas dibanding XML. XML itu perlu closing tag buat tiap elemen (<title>...</title>), sedangkan JSON cukup "title": "..." aja, jadi ukuran datanya lebih kecil dan lebih cepat buat dikirim lewat network. Lalu karena JSON itu sebenernya format objek JavaScript, jadi pas dipake di web (yang mayoritas logic client sidenya pake JS), dia bisa langsung diparse tanpa perlu library tambahan, tinggal JSON.parse() aja. XML biasanya butuh parser XML yang lebih berat. Selain itu JSON juga lebih gampang dibaca manusia, strukturnya lebih simple, jadi pas dipake buat komunikasi API modern (kayak REST API), JSON udah jadi standar yang paling umum dipake sekarang.

3.  # Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

Alurnya kira-kira gini: waktu ada request masuk ke url yang aku daftarin (misal /api/experience/), Django manggil view get_experience_json. Di situ aku ambil semua data experience dari database pake Experience.objects.all(), hasilnya berupa QuerySet yang isinya objek-objek Python (instance model Django). Nah, objek ini tidak bisa langsung dikirim sebagai response HTTP, soalnya HTTP itu cuma bisa ngirim teks/byte, sementara objek model Django itu struktur data yang spesifik buat Python doang (ada method, relasi ke model lain, dll yang tidak dimengerti di luar Python). Makanya perlu diserialize dulu pake serializers.serialize("json", experience_list), biar objek itu berubah jadi string JSON yang formatnya universal. Baru setelah itu aku bungkus jadi HttpResponse dengan content_type="application/json", supaya client (misal browser atau aplikasi lain) tau cara bacanya. Jadi intinya, serialization itu penting buat jembatanin antara struktur data internal Django yang kompleks sama format data yang bisa dipahami sama sistem lain di luar Python.

AI Disclosure Tugas 3 : Dalam implementasi CRUD Experience (form, view create/update/delete, sama JSON serialization), saya menggunakan AI buat membantu menjelaskan konsep ModelForm, alur create ,pdate,delete di Django, sama cara kerja serialization ke JSON. AI juga membantu memberi contoh struktur kode form, view, dan template supaya lebih gampang dipahami sebelum aku sesuain sama struktur projectku sendiri.Beberapa hal yang aku temukan dan perbaiki sendiri:Sempet ada NoReverseMatch error karena di navbar masih ada {% url 'main:add_experience' %}, padahal nama url yang aku daftarin di urls.py itu create_experience. Aku cari manual pake Select-String di terminal buat nemuin baris mana yang masih salah nama, terus benerin sendiri.Gambar thumbnail experience sempet nggak muncul walaupun datanya udah keisi. Ternyata di template aku salah nulis nama field, aku pake exp.thumbnail_url padahal field di model namanya hanya thumbnail. Karena Django Template Language tidak error kalau atributnya tidak ada (cuma dianggap kosong), bugnya jadi tidak kelihatan sampai aku cek manual satu-satu antara models.py sama template.Ada bug serupa juga di bagian status "Sedang berlangsung" ,aku pake exp.end_date di template padahal field di model namanya ended_at. Ini juga aku temuin sendiri pas ngebandingin ulang field model sama yang dipanggil di template.

Sumber  : https://jsonforms.io/docs/
