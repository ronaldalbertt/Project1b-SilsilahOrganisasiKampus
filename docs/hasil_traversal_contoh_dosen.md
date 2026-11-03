# Hasil Traversal Contoh Struktur dari Dosen — 18 Node

Contoh ini terpisah dari Tree utama UIN Suska Riau yang berjumlah 27 node. Contoh ini dipertahankan untuk memperlihatkan traversal pada diagram latihan.

- Jumlah node: 18
- Tinggi: 5 edge
- Jumlah level: 6

## Aturan traversal

- **Preorder:** node saat ini, kemudian anak-anaknya.
- **Inorder adaptasi:** subtree anak pertama, node saat ini, kemudian subtree anak berikutnya. Ini adaptasi karena struktur contoh adalah General Tree.
- **Postorder:** seluruh anak diproses terlebih dahulu, kemudian node saat ini.

## Urutan Postorder

1. Senat Universitas
2. Wakil Rektor I
3. Wakil Rektor II
4. Wakil Rektor III
5. Wakil Dekan I
6. Wakil Dekan II
7. Wakil Dekan III
8. Sekretaris Program Studi
9. Asisten Laboratorium
10. Teknisi Laboratorium
11. Kepala Laboratorium Komputer
12. Mahasiswa Bimbingan
13. Dosen Pembimbing Akademik
14. Dosen Pengampu Mata Kuliah
15. Koordinator Dosen
16. Ketua Program Studi Teknik Informatika
17. Dekan Fakultas Sains dan Teknologi
18. Rektor

**Koreksi penting:** Dosen Pengampu Mata Kuliah harus muncul sebelum Koordinator Dosen karena keduanya merupakan anak Koordinator Dosen. Postorder mengunjungi anak sebelum parent.
