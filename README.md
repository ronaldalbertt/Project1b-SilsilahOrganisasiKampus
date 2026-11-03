# Proyek 1b — Silsilah Organisasi UIN Suska Riau

## Deskripsi

Proyek ini merupakan purwarupa (prototype) aplikasi sederhana untuk memodelkan hierarki organisasi Universitas Islam Negeri Sultan Syarif Kasim Riau menggunakan struktur data **General Tree**.

General Tree dipilih karena satu node dapat memiliki lebih dari dua anak. Struktur ini sesuai untuk menggambarkan hubungan hierarkis yang terdiri dari berbagai kelompok organisasi, unit, fakultas, dan jabatan.

Program dibuat menggunakan Python dengan pendekatan Object-Oriented Programming (OOP).

## Struktur Data Tree

Setiap node pada program memiliki empat atribut:

| Atribut | Keterangan |
|---|---|
| `id_node` | ID unik untuk setiap node |
| `nama` | Menyimpan nama orang atau nama unit |
| `jabatan` | Menyimpan jabatan atau jenis unit |
| `children` | Menyimpan daftar node anak dari suatu node |

Root atau akar Tree adalah **UIN Sultan Syarif Kasim Riau**.

Struktur utama mengelompokkan organisasi menjadi tiga bagian:
1. Bagian Pengelola / Pimpinan Universitas.
2. Bagian Pertimbangan.
3. Bagian Pengawas.

Pada bagian pengelola terdapat Rektor, Wakil Rektor, delapan fakultas, Pascasarjana, biro, lembaga, dan unit lainnya.

Sebagai contoh, pada Fakultas Sains dan Teknologi terdapat hierarki Dekan Fakultas, Ketua Program Studi Teknik Informatika, dan Dosen Teknik Informatika.

Struktur ini merupakan pemodelan sederhana untuk kebutuhan proyek, bukan representasi lengkap seluruh hubungan pelaporan resmi universitas.

## Data Awal

Struktur Tree utama memiliki:
- Jumlah node: **27 node**
- Tinggi Tree: **5 edge**
- Jumlah level: **6 level**
- Jumlah anak terbanyak pada satu node: **17 node**

Distribusi node berdasarkan level:

| Level | Jumlah Node |
|---|---:|
| 0 | 1 |
| 1 | 3 |
| 2 | 4 |
| 3 | 17 |
| 4 | 1 |
| 5 | 1 |
| **Total** | **27** |

Nama yang diberi label `(Contoh)` merupakan data ilustrasi, bukan pernyataan bahwa orang tersebut merupakan pejabat aktual.

## Fitur Program

Program menyediakan beberapa fitur:

1. Menampilkan struktur organisasi dalam bentuk hierarki Tree.
2. Menambahkan unit, pegawai, atau jabatan berdasarkan ID atasan.
3. Mencari data berdasarkan nama atau jabatan.
4. Menampilkan Preorder Traversal.
5. Menampilkan Inorder Traversal yang menggunakan aturan adaptasi General Tree.
6. Menampilkan Postorder Traversal.
7. Menganalisis jumlah node, tinggi, jumlah level, jumlah anak terbanyak, dan bentuk Tree.
8. Menampilkan contoh traversal terpisah sebanyak 18 node sesuai contoh soal dari dosen.

## Algoritma Traversal

Program menggunakan tiga pendekatan traversal:

### 1. Preorder Traversal
Node induk dikunjungi terlebih dahulu, kemudian dilanjutkan ke seluruh node anak secara berurutan.

### 2. Inorder Traversal (Adaptasi General Tree)
Karena Inorder umumnya digunakan pada Binary Tree, proyek ini menggunakan aturan adaptasi:
- Mengunjungi subtree anak pertama.
- Mengunjungi node saat ini.
- Mengunjungi subtree anak berikutnya secara berurutan.

### 3. Postorder Traversal
Seluruh node anak dikunjungi terlebih dahulu, kemudian node induknya.

## Cara Menjalankan Program

Pastikan Python sudah terpasang. Buka terminal pada direktori utama repository, kemudian jalankan:

```bash
python -m src.code01_organisasi.main
```

Setelah program berjalan, menu utama akan ditampilkan. Pengguna dapat memilih fitur sesuai nomor menu yang tersedia.

## Menjalankan Pengujian

Untuk menjalankan pengujian program, gunakan perintah:

```bash
python -m unittest discover -s tests -v
```

Pengujian mencakup operasi penyisipan, pencarian, traversal, jumlah node, tinggi Tree, serta validasi struktur organisasi.

## Analisis Kompleksitas

Dengan `n` sebagai jumlah seluruh node pada Tree, kompleksitas waktu dari beberapa operasi adalah:

| Operasi | Kompleksitas | Keterangan |
|---|---|---|
| `insert_node()` | O(n) | Memeriksa ID duplikat dan mencari node atasan |
| `search_node()` | O(n) | Menelusuri node untuk mencari nama atau jabatan |
| Preorder Traversal | O(n) | Mengunjungi seluruh node satu kali |
| Inorder Traversal | O(n) | Mengunjungi seluruh node satu kali |
| Postorder Traversal | O(n) | Mengunjungi seluruh node satu kali |
| `count_nodes()` | O(n) | Menghitung seluruh node |
| `height()` | O(n) | Menelusuri cabang untuk mencari kedalaman maksimum |
| `level_counts()` | O(n) | Menghitung node pada setiap level |
| `max_children()` | O(n) | Memeriksa jumlah anak pada setiap node |

Struktur Tree yang dibuat memiliki banyak cabang, tetapi tidak seimbang sempurna. Sebagian besar cabang berhenti pada level yang lebih awal, sedangkan cabang Fakultas Sains dan Teknologi memiliki kedalaman lebih besar.

Pencarian nama atau jabatan tetap memiliki kompleksitas O(n) karena General Tree ini tidak menggunakan aturan pengurutan seperti Binary Search Tree.
