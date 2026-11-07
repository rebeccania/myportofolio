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

# Progress Minggu 4 :
- Mengimplementasikan sistem autentikasi lengkap meliputi fitur Register (register), Login (login_user), dan Logout (logout_user) menggunakan built-in form Django (UserCreationForm dan AuthenticationForm).
- Menambahkan manajemen cookie untuk melacak waktu login terakhir pengguna (last_login) pada response saat proses login berhasil, serta menampilkannya di halaman utama (show_main).
- Menerapkan pembatasan hak akses berbasis peran (Role-Based Access Control) menggunakan dekorator @login_required dan pengecekan manual kondisi request.user.is_superuser serta keanggotaan grup Editor (request.user.groups.filter(name='Editor').exists()) pada fitur Create, Edit, Delete portofolio. 
- Menambahkan relasi ManyToManyField ke model User pada model Project (fitur interaktif Star) untuk mendukung sistem pemberian dan pembatalan star dengan batasan maksimal satu star per pengguna.
- Membuat fungsi view toggle_star berbasis metode POST dengan pengamanan @login_required serta token {% csrf_token %} untuk memproses aksi tambah/hapus star secara dinamis.
- Melakukan pembaruan pada templat HTML (project.html dan experience.html) untuk menampilkan jumlah total Star, status tombol interaktif, serta menyembunyikan atau menampilkan tombol Create/Edit/Delete secara kondisional berdasarkan hak akses akun yang sedang login.

AI Disclosure : Dalam mengimplementasikan sistem autentikasi (register, login, logout, pencatatan cookie last_login), mekanisme pembatasan hak akses (Superuser dan Editor), serta fitur interaktif pemberian Star (ManyToManyField dan fungsi toggle_star), saya memanfaatkan bantuan AI untuk memahami konsep dasar dekorator keamanan Django, struktur penulisan query many-to-many, serta cara menyisipkan pengecekan grup pengguna di dalam fungsi view dan templat. AI juga membantu memberikan contoh kerangka kode penanganan session dan CSRF protection.Beberapa kendala yang saya temukan dan selesaikan sendiri:Sempat terjadi error NoReverseMatch saat menambahkan tautan menu dan tombol aksi karena ketidaksesuaian penamaan path di dalam urls.py dengan tag {% url %} di dalam templat HTML. Saya mengecek dan mencocokkan ulang daftar nama URL satu persatu secara manual.Muncul kesalahan Page Not Found (404) saat mengakses halaman edit akibat tipe data parameter di urls.py yang sebelumnya didefinisikan sebagai <int:id>, padahal model portofolio menggunakan identifikasi berbasis UUID (<uuid:id>). Saya memperbaikinya dengan menyesuaikan tipe parameter di berkas urls.py agar sinkron dengan model.Sempat keliru mendefinisikan variabel kondisi is_editor di dalam context view, sehingga tombol Edit sempat tidak muncul pada akun yang sudah dimasukkan ke dalam grup Editor. Saya memperbaikinya dengan menuliskan fungsi pengecekan grup request.user.groups.filter(name='Editor').exists() secara eksplisit pada fungsi view terkait.

Sumber  : 
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Sessions
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Forms

# Progress Minggu 5:
- Mengubah experience.html supaya hanya merender kerangka halaman, sedangkan datanya diambil terpisah lewat fetch() ke endpoint JSON.
- Merakit JSON pakai JsonResponse biar bisa menyisipkan info star (star_count, is_starred, starred_by_names) yang tidak bisa dilakukan serializers.serialize bawaan Django.
- Menambahkan field starred_by (ManyToMany ke User) di model, bikin migration baru, dan menambah view toggle_star_experience yang mengembalikan JSON.
- Menambahkan search by judul experience via AJAX dengan jeda 300ms supaya request cuma dikirim setelah user berhenti mengetik.
- Mengganti halaman form terpisah jadi modal Popover API yang dibungkus {% if user.is_superuser %} biar cuma muncul buat pemilik portofolio.
-  Menambahkan view create_experience_ajax yang validasi pakai ExperienceForm dan mengembalikan JSON 201/400/403, serta mengubah delete jadi AJAX biar kartu langsung hilang tanpa reload.
- Memanfaatkan showToast() dari Tutorial 5 untuk menampilkan notif sukses saat data ditambah/dihapus dan notif error dari pesan validasi server.
-  Menambahkan escapeHtml() di JavaScript untuk semua nilai yang masuk innerHTML, plus clean_title/clean_description/clean_category dengan strip_tags di form.
-  Membungkus form dalam card yang center di halaman, mengubah input jadi gelap sesuai tema, dan mengakali autofill Chrome pakai -webkit-box-shadow inset biar field password gak tetep putih.

### Tugas 5:

1. # Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

Debouncing itu adalah teknik untuk menunda eksekusi sebuah fungsi sampai ada jeda waktu tertentu tanpa event baru yang muncul.Caranya dengan membatalkan timer lama (clearTimeout) lalu membuat timer baru (setTimeout) setiap kali user mengetik. Di fitur pencarian AJAX, tanpa debouncing setiap huruf yang diketik langsung memicu fetch(), jadi ngetik "Django" bisa kirim 6 request berturut-turut padahal hasil akhirnya cuma butuh 1. Dengan debouncing 300ms, request baru dikirim setelah user benar-benar berhenti mengetik, sehingga beban server jauh berkurang dan bandwidth lebih hemat. Teknik ini juga mencegah race condition, di mana request lama yang selesai belakangan bisa menimpa hasil pencarian terbaru yang seharusnya ditampilkan. User tetap merasakan pencarian yang responsif karena delaynya cuma sepersekian detik dan tidak terasa mengganggu. Intinya, debouncing itu penting supaya pencarian real-time tetap efisien tanpa mengorbankan pengalaman pengguna.

2. # Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

fetch() itu mengembalikan Promise, bukan data langsung, jadi tanpa await variabel response isinya Promise dan saat kita memanggil response.json() akan terjadi error karena Promise tidak punya method tersebut. Keyword await membuat JavaScript menunggu Promise selesai diproses dulu sebelum lanjut ke baris berikutnya. Await hanya bisa dipakai di dalam async function, makanya semua handler seperti fetchProjects() dan addProject() aku deklarasikan dengan keyword async di depannya. Kalau await tidak dipakai, kode setelahnya akan jalan duluan sebelum data datang, sehingga nilai yang mau ditampilkan menjadi undefined atau malah bikin error karena strukturnya belum siap. Ini juga yang bikin kode jadi susah dibaca di zaman sebelum ada async/await, karena harus pakai callback bersarang atau .then() berantai. Jadi kesimpulannya, await berfungsi menjaga urutan eksekusi kode asinkron supaya hasilnya bisa langsung dipakai di baris berikutnya.

3. # Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

XSS (Cross-Site Scripting) adalah jenis serangan di mana penyerang berhasil menyisipkan kode JavaScript jahat ke halaman web, lalu kode itu dieksekusi di browser korban  misalnya <img src="x" onerror="alert('XSS!')"> yang otomatis trigger alert saat gambarnya gagal dimuat. Di template Django, setiap variabel yang ditampilkan lewat {{ variabel }} otomatis diescape oleh fitur auto-escaping bawaan, jadi karakter seperti <, >, &, dan " diubah jadi entity HTML (&lt;, &gt;, dst) dan browser menampilkannya sebagai teks biasa, bukan tag aktif. Perlindungan itu hilang begitu kita pindah ke AJAX, karena data JSON disusun pakai template literal (backtick) lalu dimasukkan ke DOM lewat innerHTML, dan innerHTML menerjemahkan string sebagai HTML sungguhan. Django tidak bisa membantu lagi di titik ini karena datanya sudah keluar dari template engine dan sampai di browser sebagai string mentah. Makanya saya menambahkan fungsi escapeHtml() di JavaScript untuk membungkus setiap nilai teks yang masuk ke innerHTML, plus method clean_title, clean_description, dan clean_category dengan strip_tags di ExperienceForm sebagai lapisan kedua di sisi server. Dua lapisan ini disebut defense in depth , kalau satu lapis kebobolan, masih ada lapis lainnya yang menahan.

AI Disclosure : Dalam ngerjain Tugas 5 ini, saya memanfaatkan AI buat bantu memahami pola AJAX end-to-end yang harus diterapin ke halaman Experience mulai dari nyusun endpoint JSON pake JsonResponse, ngatur modal form pakai Popover API, sampe ngehandle CSRF token di request fetch(). AI juga bantu ngejelasin konsep-konsep yang agak tricky kayak debouncing, AbortController buat ngecancel request lama, dan cara ngeescape HTML biar aman dari XSS.Beberapa hal yang saya temukan dan selesaikan sendiri:Sempat error ImportError: cannot import name 'delete_project' pas nambahin create_experience_ajax di urls.py. Ternyata fungsi delete_project kehapus pas saya rewrite views.py. Saya cek satu-satu pakai findstr di terminal, terus tambahin balik fungsi yang ilang. Sekalian saya rapihin import di urls.py jadi multi-line biar kalau ada yang salah lebih gampang keliatan.
Tombol "Tambah Project" awalnya turun ke baris baru, gak sejajar sama "Test Toast". Ternyata karena tombolnya ditaruh di luar <div class="project-header">. Saya perbaiki dengan mindahin ke dalam wrapper .project-header__actions biar dua tombolnya nempel di kanan.
Field password di halaman login sempet tetep putih walaupun udah dikasih CSS. Setelah buka DevTools → Inspect, ternyata Chrome autofill ngeoverride background pakai -webkit-autofill. Solusinya pake -webkit-box-shadow: 0 0 0 1000px ... inset yang cuma bisa di-override sama cara itu.

Sumber :
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API
https://www.django-rest-framework.org/topics/ajax-csrf-cors/

# Progress Minggu 10 :
- Install dan setup Django REST Framework (DRF), terus bikin ProjectSerializer, permission IsPortfolioOwnerOrReadOnly, API view pake @api_view di main/api_views.py, dan route di main/api_urls.py di bawah prefix /api/v1/. Ini buat Tutorial 07 di bagian Projects.
- Halaman Projects aku ubah biar ngambil, nyari, nambah, ngasih star, dan hapus data lewat API baru pake fetch(), plus header X-CSRFToken dan escapeHtml tetep dipake.
- Nulis test pake APITestCase buat Tutorial 07 (16 test), termasuk test CSRF pake APIClient(enforce_csrf_checks=True).
- Untuk Tugas 6, aku terapin pola yang sama di bagian Experience: bikin ExperienceSerializer dengan fields eksplisit, field star yang read-only (star_count, is_starred, starred_by_names), dan validate_<field> pake strip_tags.
- Bikin permission IsPortfolioOwnerOrEditorOrReadOnly buat 4 peran: pengunjung cuma baca, user biasa bisa star, Editor bisa PUT/PATCH tapi nggak bisa bikin atau hapus, dan superuser bisa semuanya.
- Bikin view experience_list, experience_detail, dan experience_star pake SessionAuthentication. Pencarian dari Tugas 5 aku pindahin jadi query param ?title=. Endpoint didaftarin di /api/v1/experience/ dengan nama experience-list, experience-detail, experience-star.
- Halaman Experience diubah total: tampil, cari, tambah, star, hapus, dan edit (modal edit baru pake PATCH) semua lewat API tanpa reload. Error 400 dan 403 dari API ditampilin lewat toast.
- Bikin modal edit yang rapi di tengah layar buat Experience dan Projects, terus tombol Edit Projects aku ganti dari link ke halaman form lama jadi modal yang manggil API.
- Nulis tests_api_experience.py yang ngecover tiap peran, ngecek isi database pas penolakan, validasi, star, dan CSRF. Hasil akhir python manage.py test main lulus semua.
### Tugas 6:

1. # Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!

REST (Representational Transfer State) itu gaya arsitektur buat ngerancang web API, bukan library atau format data. Ada tiga ide utamanya yang aku praktekin di tutorial. Pertama, data diperlakukan sebagai resource, jadi URLnya nunjuk ke datanya, misal /api/v1/experience/ buat kumpulan experience dan /api/v1/experience/<id>/ buat satu experience. Kedua, HTTP method yang nentuin tindakannya: GET buat baca, POST buat bikin, PUT/PATCH buat ngubah, DELETE buat hapus, jadi nggak perlu nulis tindakannya di URL kayak /delete/ atau /add-ajax/. Ketiga, client dan server tukeran representasi data (JSON), bukan objek Python atau baris database langsung.

Makanya cuma ngembaliin JSON belum cukup disebut RESTful. Yang nentuin itu cara APInya diatur. Kalau aku bikin endpoint kayak /projects/add-ajax/ atau /projects/<id>/delete/ yang ngembaliin JSON, itu tetep belum RESTful karena tindakannya ditulis di URL dan methodnya nggak dimanfaatin. API baru dibilang RESTful kalau resource, method, dan status code HTTPnya konsisten dan jelas (201 buat created, 204 buat deleted, 404 buat nggak ketemu, dst).

Beda PUT dan PATCH: PUT itu ngirim representasi pengganti yang lengkap, jadi semua field wajib dikirim. PATCH cuma ngirim field yang mau diubah aja (di DRF pake partial=True). Di tugasku, kalau aku PUT cuma dengan title, hasilnya 400 karena description dan field wajib lain nggak ikut. Contoh pemakaian: PATCH cocok buat modal edit yang cuma ganti judul pengalaman, soalnya field lain nggak perlu dikirim ulang dan nggak ketimpa. PUT cocok kalau mau nimpa seluruh data sekaligus, misalnya form edit lengkap yang selalu ngirim semua field.

2. # Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
Serializer itu jembatan dua arah antara objek model Django dan data JSON. Pas GET, serializer ngubah objek model jadi tipe data Python yang bisa dirender jadi JSON (serialization). Pas POST/PUT/PATCH, serializer ngubah input dari klien jadi data yang udah divalidasi dan siap disimpan (deserialization), lewat is_valid() terus save(). Dia juga yang nentuin field apa aja yang boleh keluar masuk, jadi kontrak datanya jelas. Contohnya di ExperienceSerializer, fields ditulis eksplisit dan star_count, is_starred, starred_by_names bersifat read-only, jadi nggak bisa dipalsuin klien dan data sensitif kayak email atau password nggak ikut kebawa.

Keuntungannya dibanding ngerakit dictionary manual kayak get_experience_json di Tutorial 05: aku nggak perlu nulis ulang dictionary per field di tiap view, validasinya ikut jadi satu tempat (validate_title dan strip_tags misalnya) jadi nggak diulang di tiap view, error validasi otomatis jadi response 400 per field, dan kodenya bisa dipake ulang buat daftar, detail, create, sama update. Kalau manual, tiap ada endpoint baru aku harus ngulang pola yang sama dan gampang ada yang kelupaan atau beda-beda antar endpoint.

3. # Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?

Autentikasi itu jawab pertanyaan “kamu siapa?”, sedangkan otorisasi jawab “kamu boleh ngapain?”. Di DRF dua-duanya dipisah: authentication class (di tugasku SessionAuthentication) yang ngisi request.user dari session login, lalu permission class (IsPortfolioOwnerOrEditorOrReadOnly, IsAuthenticated) yang mutusin request itu boleh diterusin atau nggak. Urutannya autentikasi dulu, baru permission, jadi misalnya user biasa yang mau PATCH experience tetep dikenali sebagai user biasa, tapi ditolak 403 di tahap permission.

Hak akses harus dicek di server karena nyembunyiin tombol itu cuma ngatur tampilan, bukan keamanan. Siapa pun bisa kirim request langsung lewat Console browser, Postman, atau curl tanpa lewat tombol sama sekali. Aku bahkan ngetes ini sendiri: tombol Edit disembunyiin buat user biasa, tapi kalau aku kirim PATCH lewat Console, server tetep nolak 403 dan datanya nggak berubah. Kalau cuma ngandelin template, ya siapa aja yang tau URL APInya bisa ngubah atau ngehapus data.

4. # Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

SessionAuthentication ngandelin cookie session yang otomatis dikirim browser di tiap request ke domain yang sama. Itu artinya kalau ada situs jahat yang nyuruh browser user (yang lagi login) ngirim request POST/PUT/PATCH/DELETE ke API kita, cookie sessionnya ikut kekirim dan server ngira itu request yang sah. Makanya DRF tetep minta token CSRF buat request yang ngubah data, biar server bisa mastiin request itu datang dari halaman yang emang dirender sama situs kita sendiri (karena situs jahat nggak bisa baca token itu). Di frontend, token diambil dari cookie csrftoken terus dikirim lewat header X-CSRFToken. Makanya juga nggak boleh nambahin @csrf_exempt cuma buat ngilangin error 403.

force_authenticate nggak cukup karena dia langsung nyetel user di request dan ngelewatin proses session, jadi pengecekan CSRF nggak pernah jalan sama sekali. Test pake itu bakal lulus walaupun perlindungan CSRFnya rusak. Buat buktiin CSRF beneran jalan, aku pake APIClient(enforce_csrf_checks=True) dan .login() yang bikin session sungguhan: POST tanpa token harus ditolak 403 (dan data di database nggak bertambah), sedangkan POST dengan token dari cookie harus berhasil 201.

AI Disclosure Tugas 6 : Dalam mengerjakan Tutorial 07 dan Tugas 6, saya menggunakan AI buat membantu menjelaskan alur kerja DRF dan nyusun kode awal buat ExperienceSerializer, permission class, API view, route, test APITestCase, sama JavaScript fetch() di halaman Experience dan Projects. AI juga bantu nyusun CSS modal edit dan pesan commit. Semua kode itu aku sesuain sama struktur proyekku sendiri (nama model, field, ID elemen, dan template yang udah ada) dan aku jalanin sendiri buat dites. Beberapa hal yang aku temuin dan perbaiki sendiri: Sempet muncul TemplateSyntaxError: Unclosed tag 'block' waktu python manage.py test main karena {% endblock content %} di experience.html ketiban pas ngegantiin blok script, jadi aku cek ulang bagian akhir file dan nambahin lagi. Modal edit awalnya jelek dan nempel di pojok kiri atas karena reset * { margin: 0 } di CSS-ku ngilangin margin bawaan <dialog>, dan tombol Edit-nya transparan, jadi aku bikin style modal yang rapi di tengah dan tombol Editnya aku samain kayak di Projects. Tombol Edit Projects awalnya masih ke halaman form lama dan kalau non-superuser nyoba nyimpen malah muncul halaman Forbidden, bukan toast, jadi aku ganti jadi modal yang manggil API. Akun Editor di Experience tombol Edit-nya muncul tapi nggak ngapa-ngapain waktu diklik. Aku cek lewat console.log dan ternyata IS_EDITOR udah bener, lalu ketemu penyebabnya modal edit ada di dalam blok {% if user.is_superuser %} jadi Editor nggak dapet elemen modalnya, terus aku pisahin blok itu. Aku juga mastiin sendiri aturan perannya ke dokumen tutorial dan memutuskan Projects tetap owner-only sesuai tutorial, sedangkan empat peran dipake di Experience.

Sumber: https://www.django-rest-framework.org/
