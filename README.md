Nama : Rebeccaniaga Napitupulu
NPM : 2506598394
Kelas : PBP E
Dosen : Pak Daya

### Tugas 1

1. Saya menggunakan elemen semantik HTML5 dalam merancang struktur halaman portofolio saya. Saya memakai elemen <header> untuk bagian navbar, serta elemen <section> untuk membagi halaman menjadi beberapa bagian utama, yaitu <section id="home"> untuk bagian hero, <section id="about"> untuk bagian perkenalan diri, dan <section id="education"> untuk bagian riwayat pendidikan yang saya tambahkan sebagai section baru.

Penggunaan elemen semantik ini sangat membantu saya, terutama ketika saya sedang menyusun ulang kode dari struktur berbasis Tailwind menjadi CSS murni. Karena setiap section memiliki identitas (id) yang jelas, saya dapat dengan mudah menelusuri bagian mana yang sedang saya edit tanpa harus membaca ulang keseluruhan kode dari awal. Selain itu, id pada tiap section juga saya hubungkan dengan menu navigasi, sehingga ketika pengguna mengklik menu tersebut, halaman akan otomatis melakukan scroll menuju bagian yang dituju. Apabila saya hanya menggunakan elemen <div> tanpa struktur semantik yang jelas, proses pengelolaan dan pengembangan halaman akan menjadi lebih sulit dan membingungkan.

Saya belum menggunakan elemen <article> maupun <aside> karena konten yang saya buat masih saling berkaitan erat dengan section induknya dan belum memerlukan pemisahan lebih lanjut sebagai konten yang berdiri sendiri.

2. Tantangan responsive yang paling saya rasakan muncul saat saya mengubah struktur layout dari berbasis Tailwind menjadi CSS manual. Tantangan terbesar terletak pada bagian timeline Education. Pada tampilan desktop, kartu timeline ditampilkan secara zig-zag bergantian kiri dan kanan dari garis tengah. Namun ketika ditampilkan pada layar kecil, tata letak tersebut menjadi tidak rapi apabila tetap dipaksakan dalam bentuk zig-zag. Oleh karena itu saya menggunakan breakpoint @media (min-width: 768px) agar tampilan zig-zag hanya diterapkan pada layar desktop, sedangkan pada tampilan mobile seluruh kartu ditampilkan sejajar dalam satu kolom.

Selain itu, menu navigasi pada bagian tengah header juga menjadi tantangan tersendiri. Ketika ditampilkan pada layar ponsel, menu tersebut menjadi terlalu sempit dan tidak proporsional, sehingga saya memutuskan untuk menyembunyikan menu tersebut pada tampilan mobile dan hanya menyisakan logo serta tombol Hire Me.

Dalam mengevaluasi elemen mana yang perlu diprioritaskan, saya mempertimbangkan elemen apa yang paling penting untuk dilihat terlebih dahulu oleh pengunjung pada layar kecil. Saya menyimpulkan bahwa foto dan nama merupakan elemen utama yang harus tetap jelas dan tidak berubah posisi secara drastis, sementara elemen dekoratif seperti badge kecil maupun efek visual lainnya dapat menyesuaikan secara otomatis.

3. Batasan utama yang saya rasakan adalah seluruh konten harus ditulis manual di dalam HTML. Sebagai contoh, saat mengganti ikon media sosial, saya harus mencari dan menambahkan kode SVG satu per satu karena pustaka ikon yang saya pakai sudah tidak menyediakan ikon brand tersebut. Saya juga sempat kesulitan saat berpindah ke Django, karena path pemanggilan berkas statis (CSS, gambar, PDF) yang sebelumnya berfungsi ternyata tidak terbaca dan harus diganti menggunakan {% static %}. Selain itu, halaman ini juga belum memiliki interaksi nyata dengan pengunjung, misalnya tombol Download CV yang hanya berupa tautan statis tanpa fitur tambahan apa pun.

Berdasarkan batasan tersebut, pada iterasi selanjutnya menggunakan arsitektur MVT di Django, saya ingin menyimpan data Education dan Projects dalam bentuk model basis data agar dapat dikelola melalui admin panel tanpa mengubah kode HTML, serta menambahkan formulir kontak sederhana agar pengunjung dapat mengirim pesan langsung dari halaman portofolio.

AI Disclosure:Saya menggunakan bantuan AI (Chatgpt) untuk konversi Tailwind ke CSS murni, penyusunan section baru, dan debugging saat deployment ke PWS. Beberapa keterbatasan yang saya temukan dan perbaikan manual yang saya lakukan: pertama, AI membantu menerjemahkan class utility Tailwind menjadi CSS custom, namun saya tetap perlu memverifikasi ulang nilai padding, warna, dan breakpoint responsive secara manual agar sesuai tampilan aslinya. Kedua, AI awalnya menyarankan pustaka Lucide untuk seluruh ikon, tetapi ikon GitHub, LinkedIn, dan Instagram tidak muncul karena versi terbaru Lucide sudah tidak menyediakan ikon brand, sehingga saya meminta solusi alternatif dan menerapkan SVG inline sebagai gantinya lalu memverifikasinya manual di browser. Ketiga, path CSS, gambar, dan CV yang sebelumnya berfungsi ternyata tidak terbaca saat dijalankan lewat Django; AI menjelaskan penggunaan {% load static %} dan {% static %}, yang kemudian saya terapkan dan uji manual satu per satu. Secara umum, AI mempercepat proses penulisan kode dan penjelasan konsep, tetapi saya tetap melakukan verifikasi dan perbaikan manual pada bagian yang berkaitan dengan pustaka pihak ketiga yang sudah usang dan perbedaan lingkungan antara HTML statis biasa dengan proyek Django.

Progress Mingguan :
- Membangun halaman "About Me" dasar sesuai Tutorial 01 dengan data placeholder.
- Mengisi ulang seluruh konten dengan data pribadi asli (nama, NPM, foto, bio).
- Merancang ulang tampilan menjadi tema dark purple & amber, menggantikan seluruh class Tailwind menjadi CSS murni yang ditulis manual di style.css.
- Menambahkan section baru Education berupa timeline riwayat pendidikan dengan layout zig-zag di desktop dan satu kolom di mobile.
- Memperbaiki bug ikon media sosial (GitHub, LinkedIn, Instagram) yang tidak muncul karena pustaka Lucide tidak lagi menyediakan ikon brand tersebut diganti dengan SVG custom.
- Mengonfigurasi pemanggilan file statis (CSS, gambar, PDF CV) menggunakan {% load static %} dan {% static %} agar dapat terbaca oleh Django.
- Deploy proyek ke PWS dan menyelesaikan konflik merge antara commit lokal dengan commit awal dari server.

Tentang Proyek : 
Proyek ini merupakan Tugas Individu mata kuliah Pemrograman Berbasis Platform (PBP), yang melanjutkan langsung dari Tutorial 01. Halaman ini berisi:
- Home (Hero Section) : perkenalan singkat, foto profil, dan tautan media sosial.
- About Me : enam karakteristik personal yang menggambarkan diri saya, ditampilkan dalam layout grid dengan efek hover.
- Education : timeline riwayat pendidikan dari SD hingga perkuliahan saat ini, ditampilkan dalam bentuk garis waktu zig-zag yang responsif.

Tech Stack:
- Django (struktur proyek, template rendering, static files)
- HTML5 (elemen semantik: <header>, <section>)
- CSS3 murni (custom properties, Flexbox, Grid, media query tanpa framework CSS)
- Lucide Icons (untuk ikon generik) & SVG inline custom (untuk ikon brand GitHub/LinkedIn/Instagram)
- Deployment: PWS (Pacil Web Service)
