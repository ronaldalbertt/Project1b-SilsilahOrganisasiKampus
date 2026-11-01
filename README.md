# Proyek 1b — Silsilah Organisasi FST

Program ini memodelkan hierarki Fakultas Sains dan Teknologi (FST), UIN Sultan Syarif Kasim Riau, menggunakan struktur data **General Tree**.

## Cakupan data

Root Tree adalah Dekan FST. Data contoh mencakup:
- 3 Wakil Dekan;
- 6 Program Studi, masing-masing dengan Ketua dan Sekretaris;
- 7 Kepala Laboratorium;
- Kepala Bagian Tata Usaha dan Kelompok Jabatan Fungsional dan Pelaksana.

Total data awal adalah **31 node** dengan tinggi **2 edge (3 level)**. Nama orang yang diawali "Nama ..." merupakan placeholder, bukan klaim nama pejabat aktual.

Kelompok Program Studi dan Laboratorium pada diagram FST merupakan pengelompokan visual, bukan jabatan tersendiri. Garis koordinasi KPM/PMP tidak dimasukkan sebagai relasi parent-child pada Tree.

## Fitur program

1. Menampilkan struktur organisasi.
2. Menambahkan pegawai atau jabatan berdasarkan ID atasan.
3. Mencari nama atau jabatan berdasarkan kata kunci (tidak peka huruf besar/kecil).
4. Menjalankan preorder traversal.
5. Menjalankan inorder adaptasi untuk General Tree.
6. Menjalankan postorder traversal.
7. Menghitung jumlah node.
8. Menampilkan tinggi dan ringkasan struktur Tree.
9. Menjalankan contoh traversal 18 node sesuai gambar dosen untuk pengisian nomor 11.

## Struktur folder

```text
Project1b-SilsilahOrganisasi/
├── docs/
│   ├── class_diagram.md
│   ├── struktur_tree_organisasi_fst.md
│   └── hasil_traversal_contoh_dosen.md
├── src/
│   ├── code01_organisasi/
│   │   └── main.py
│   ├── data/
│   │   ├── organization_data.py
│   └── traversal_example.py
│   └── models/
│       ├── tree_node.py
│       └── organization_tree.py
├── tests/
│   └── test_organization_tree.py
├── README.md
└── .gitignore
```

## Cara menjalankan

Jalankan dari direktori utama repository:

```bash
python -m src.code01_organisasi.main
```

## Menjalankan pengujian

```bash
python -m unittest discover -s tests -v
```

## Kompleksitas waktu

Dengan n sebagai jumlah node:

| Operasi | Kompleksitas waktu | Keterangan |
|---|---:|---|
| insert_node | O(n) | Mencari ID atasan dan memeriksa ID duplikat |
| search_node | O(n) | Menelusuri node untuk mencocokkan nama/jabatan |
| preorder | O(n) | Mengunjungi setiap node satu kali |
| inorder adaptasi | O(n) | Mengunjungi setiap node satu kali |
| postorder | O(n) | Mengunjungi setiap node satu kali |
| count_nodes | O(n) | Menghitung setiap node |
| height | O(n) | Menelusuri seluruh node untuk mencari kedalaman maksimum |

General Tree ini tidak menggunakan aturan pengurutan seperti Binary Search Tree. Karena itu, pencarian nama/jabatan tidak otomatis menjadi O(log n) meskipun bentuk gambarnya tampak seimbang.

## Catatan inorder

Inorder secara umum merupakan traversal standar pada Binary Tree. Karena struktur proyek ini adalah General Tree, implementasi inorder menggunakan aturan adaptasi yang dinyatakan di kode: subtree anak pertama, node saat ini, kemudian subtree anak berikutnya sesuai urutan daftar children.

## Diagram

- [Class diagram](docs/class_diagram.md)
- [Struktur General Tree FST](docs/struktur_tree_organisasi_fst.md)
- [Hasil traversal contoh dosen nomor 11](docs/hasil_traversal_contoh_dosen.md)
"# Project1b-SilsilahOrganisasiKampus" 
