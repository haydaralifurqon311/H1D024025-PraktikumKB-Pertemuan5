# Sistem Pakar Diagnosa Penyakit THT

Proyek ini adalah sebuah aplikasi aplikasi Desktop (GUI) sederhana berbasis Python untuk mendiagnosa penyakit THT (Telinga, Hidung, Tenggorokan) berdasarkan sekumpulan gejala yang dipilih oleh pengguna. Aplikasi ini dikembangkan untuk penyelesaian Tugas Praktikum Kecerdasan Buatan (Sistem Pakar).

## Persyaratan (Prasyarat)

Aplikasi ini murni menggunakan modul bawaan (*built-in*) Python, sehingga Anda tidak perlu menginstal library eksternal via `pip`.
Pastikan komputer Anda hanya memiliki:
- **Python 3.x** terinstal (yang sudah disertai modul `tkinter` bawaan).

## Cara Menjalankan Aplikasi

1. Buka terminal atau *command prompt (cmd/powershell)*.
2. Arahkan direktori aktif ke folder tempat file kode ini disimpan.
3. Jalankan skrip *python* dengan perintah berikut:

```bash
python diagnosatht.py
```

## Bagaimana Kode Ini Bekerja?

Logika aplikasi ini memodelkan dua bagian esensial dari sebuah **Sistem Pakar**, yaitu **Basis Pengetahuan** (Knowledge Base) dan **Mesin Inferensi** (Inference Engine) secara sederhana:

### 1. Basis Pengetahuan (Knowledge Base)

Informasi dari kepakaran dokter direpresentasikan ke dalam kode menggunakan struktur data **Dictionary** (*key-value pair*) pada Python:
- Objek `GEJALA`: Berisi *mapping* daftar kode rujukan gejala (G1-G37) beserta deskripsinya. (Misal: `"G1": "Nafas abnormal"`).
- Objek `PENYAKIT`: Berisi daftar jenis-jenis penyakit dengan *array/list* aturan kode gejalanya masing-masing.

### 2. Antarmuka GUI (Tkinter)

- Menggunakan `tkinter` untuk meluncurkan jendela desktop.
- Semua kumpulan diagnosis gejala tersebut kemudian dirender secara berulang (perulangan *loop*) menjadi komponen *Checkbox / Checkbutton* secara dinamis.
- Agar tidak memenuhi layar penuh, frame *checklist* tersebut ditempelkan di atas elemen *Canvas* sehingga memunculkan efek *Scrollbar* ke bawah.
- Setiap *Checkbox* dikaitkan dengan variabel pelacak (dalam bentuk nilai Integer `1/0` atau `True/False`). 

### 3. Mesin Inferensi (Logika Pengolahan Diagnosa)

Pada saat Anda menekan tombol **"Diagnosa Penyakit"**, fungsi `diagnosa()` akan dipanggil dan menjalankan serangkaian proses komputasi ini:
1. **Pengumpulan Fakta (Input Himpunan)**: Program menyeleksi dan membuat sebuah *list* berisikan setiap "Kode Gejala" yang mana nilai *Checkbox*-nya tercentang (1).
2. **Pengecekan Aturan Secara Forward Chaining**: Aplikasi akan mengecek *Dictionary* list penyakit secara sekuensial. Metode ini langsung berupaya me-mencocokkan sekumpulan input (Fakta) dengan himpunan gejala yang dimiliki tiap-tiap entitas penyakit menggunakan operasi irisan `set.intersection`.
3. **Kalkulasi Akurasi**: Apabila ada irisan (*intersection*), maka artinya ada gejala yang klop. Program lalu mengkalkulasikan seberapa kuat persentasenya untuk memprediksi probabilitas dengan rumus: 
   `(Jumlah Gejala dari pengguna yang cocok / Total seluruh gejala yang seharusnya diidap pada Penyakit tesebut) * 100`  
4. **Pengurutan (Sorting)**: Keseluruhan nilai presentase penyakit akan dikumpulkan dan nilainya diurutkan dari kemiripan yang paling besar (`reverse=True`).
5. **Output**: Sebuah jendela detail pop-up memunculkan daftar dari beberapa atau satu probabilitas penyakit paling mungkin untuk dipertimbangkan.
