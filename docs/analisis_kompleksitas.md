# Analisis Implementasi dan Kompleksitas

Dengan `n` sebagai jumlah seluruh node:

| Operasi | Kompleksitas waktu | Alasan |
|---|---:|---|
| `insert_node()` | O(n) | Mencari ID duplikat dan mencari parent dengan penelusuran Tree. |
| `search_node()` | O(n) | Nama/jabatan diperiksa pada setiap node sampai seluruh kemungkinan diperiksa. |
| Preorder | O(n) | Setiap node dikunjungi satu kali. |
| Inorder adaptasi | O(n) | Setiap node dikunjungi satu kali. |
| Postorder | O(n) | Setiap node dikunjungi satu kali. |
| `count_nodes()` | O(n) | Mengunjungi dan menghitung seluruh node. |
| `height()` | O(n) | Memeriksa seluruh cabang untuk mencari jalur terdalam. |
| `level_counts()` | O(n) | Mengunjungi seluruh node sekali dengan antrean. |

## Bentuk Tree dan pencarian

Tree utama memiliki 27 node dan tinggi 5 edge. Bentuknya lebar, dengan sebagian besar cabang berhenti di level yang lebih dangkal dan satu cabang contoh FST berlanjut hingga Dosen. Karena struktur ini adalah General Tree dan nama/jabatan tidak disimpan dalam urutan pencarian, pencarian tidak bisa langsung menggunakan pembagian dua seperti pada Binary Search Tree. Karena itu, waktu pencarian kasus terburuk tetap O(n).

Tree ini cukup untuk merepresentasikan relasi hierarkis dan menjalankan traversal. Namun, jika ukuran data berkembang menjadi ribuan pegawai, dapat dipertimbangkan indeks tambahan seperti dictionary berdasarkan ID atau nama. Indeks tersebut merupakan pengembangan di luar implementasi dasar Tree ini.

## Catatan Inorder

Inorder baku lazim digunakan untuk Binary Tree. Karena instruksi tugas meminta Inorder sementara struktur yang dipilih adalah General Tree, program menggunakan aturan adaptasi eksplisit: subtree anak pertama, node saat ini, kemudian subtree anak berikutnya sesuai urutan `children`. Aturan ini harus disebut sebagai adaptasi, bukan definisi universal Inorder General Tree.
