from src.models.tree_node import TreeNode
from src.data.organization_data import create_organization_tree
from src.data.traversal_example import create_dosen_example_tree


def tampilkan_struktur(node, prefix="", is_last=True, is_root=True):
    if is_root:
        print(f"{node.id_pegawai} | {node.jabatan} | {node.nama}")
    else:
        konektor = "└── " if is_last else "├── "
        print(prefix + konektor + f"{node.id_pegawai} | {node.jabatan} | {node.nama}")

    if is_root:
        prefix_baru = ""
    else:
        prefix_baru = prefix + ("    " if is_last else "│   ")

    for index in range(len(node.children)):
        child = node.children[index]
        terakhir = index == len(node.children) - 1
        tampilkan_struktur(child, prefix_baru, terakhir, False)


def tampilkan_hasil_traversal(judul, daftar_node):
    print("\n===== " + judul + " =====")
    if len(daftar_node) == 0:
        print("Data organisasi kosong.")
        return

    for nomor, node in enumerate(daftar_node, start=1):
        print(str(nomor) + ". " + str(node))


def tampilkan_menu():
    print("\n" + "=" * 48)
    print("          SISTEM SILSILAH ORGANISASI")
    print("       FAKULTAS SAINS DAN TEKNOLOGI")
    print("=" * 48)
    print("[1] Tampilkan Struktur Organisasi FST")
    print("[2] Tambah Pegawai atau Jabatan")
    print("[3] Cari Pegawai atau Jabatan")
    print("[4] Preorder Traversal FST")
    print("[5] Inorder Traversal FST (Adaptasi General Tree)")
    print("[6] Postorder Traversal FST")
    print("[7] Hitung Jumlah Node FST")
    print("[8] Analisis Struktur Tree FST")
    print("[9] Jalankan Contoh Traversal dari Dosen (18 Node)")
    print("[0] Keluar")
    print("=" * 48)


def jalankan_contoh_dosen():
    tree_contoh = create_dosen_example_tree()

    print("\n===== STRUKTUR CONTOH DARI DOSEN =====")
    tampilkan_struktur(tree_contoh.root)
    print("\nJumlah node:", tree_contoh.count_nodes())
    print("Tinggi tree:", tree_contoh.height(), "edge")
    print("Jumlah level:", tree_contoh.height() + 1)

    tampilkan_hasil_traversal(
        "PREORDER - CONTOH DOSEN",
        tree_contoh.preorder_traversal()
    )
    tampilkan_hasil_traversal(
        "INORDER ADAPTASI - CONTOH DOSEN",
        tree_contoh.inorder_traversal()
    )
    tampilkan_hasil_traversal(
        "POSTORDER - CONTOH DOSEN",
        tree_contoh.postorder_traversal()
    )


def main():
    tree = create_organization_tree()

    print("Data organisasi FST berhasil dimuat.")
    print("Jumlah awal node:", tree.count_nodes())

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            print("\n===== STRUKTUR ORGANISASI FST =====")
            if tree.root is None:
                print("Tree masih kosong.")
            else:
                tampilkan_struktur(tree.root)

        elif pilihan == "2":
            print("\n===== TAMBAH PEGAWAI ATAU JABATAN =====")
            id_pegawai = input("ID Pegawai: ").strip()
            nama = input("Nama: ").strip()
            jabatan = input("Jabatan: ").strip()
            id_atasan = input("ID Atasan: ").strip()

            node_baru = TreeNode(id_pegawai, nama, jabatan)
            berhasil = tree.insert_node(id_atasan, node_baru)

            if berhasil:
                print("Data berhasil ditambahkan.")
            else:
                print("Gagal menambahkan data. Periksa kelengkapan data, ID duplikat, dan ID atasan.")

        elif pilihan == "3":
            print("\n===== CARI PEGAWAI ATAU JABATAN =====")
            kata_kunci = input("Masukkan nama atau jabatan yang dicari: ").strip()
            hasil = tree.search_node(kata_kunci)

            if len(hasil) == 0:
                print("Data tidak ditemukan.")
            else:
                print("Data ditemukan:", len(hasil), "hasil")
                for node in hasil:
                    print(node)

        elif pilihan == "4":
            tampilkan_hasil_traversal("PREORDER TRAVERSAL FST", tree.preorder_traversal())

        elif pilihan == "5":
            tampilkan_hasil_traversal(
                "INORDER TRAVERSAL FST (ADAPTASI GENERAL TREE)",
                tree.inorder_traversal()
            )

        elif pilihan == "6":
            tampilkan_hasil_traversal("POSTORDER TRAVERSAL FST", tree.postorder_traversal())

        elif pilihan == "7":
            print("Jumlah seluruh node FST:", tree.count_nodes())

        elif pilihan == "8":
            tinggi = tree.height()
            print("\n===== ANALISIS STRUKTUR TREE FST =====")
            print("Jenis Tree        : General Tree")
            print("Root              :", tree.root.jabatan if tree.root else "Tidak ada")
            print("Jumlah seluruh node:", tree.count_nodes())
            print("Tinggi Tree       :", tinggi, "edge")
            print("Jumlah level      :", tinggi + 1 if tinggi >= 0 else 0)
            print("Pencarian nama/jabatan memiliki kompleksitas O(n).")

        elif pilihan == "9":
            jalankan_contoh_dosen()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
