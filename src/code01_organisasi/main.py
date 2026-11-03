from src.models.tree_node import TreeNode
from src.data.organization_data import create_organization_tree
from src.data.traversal_example import create_dosen_example_tree


def tampilkan_struktur(node, prefix="", is_last=True, is_root=True):
    if is_root:
        print(f"{node.id_node} | {node.jabatan} | {node.nama}")
    else:
        konektor = "└── " if is_last else "├── "
        print(prefix + konektor + f"{node.id_node} | {node.jabatan} | {node.nama}")

    prefix_baru = "" if is_root else prefix + ("    " if is_last else "│   ")
    for index, child in enumerate(node.children):
        tampilkan_struktur(child, prefix_baru, index == len(node.children) - 1, False)


def tampilkan_hasil_traversal(judul, daftar_node):
    print(f"\n===== {judul} =====")
    if not daftar_node:
        print("Data organisasi kosong.")
        return
    for nomor, node in enumerate(daftar_node, start=1):
        print(f"{nomor}. {node}")


def tampilkan_menu():
    print("\n" + "=" * 58)
    print("     SILSILAH ORGANISASI UIN SUSKA RIAU")
    print("=" * 58)
    print("[1] Tampilkan struktur organisasi UIN Suska Riau")
    print("[2] Tambah unit / pegawai / jabatan")
    print("[3] Cari berdasarkan nama atau jabatan")
    print("[4] Preorder Traversal")
    print("[5] Inorder Traversal (adaptasi General Tree)")
    print("[6] Postorder Traversal")
    print("[7] Analisis jumlah node, tinggi, dan bentuk Tree")
    print("[8] Contoh traversal 18 node dari Soal 11")
    print("[0] Keluar")
    print("=" * 58)


def tampilkan_analisis(tree):
    level_counts = tree.level_counts()
    print("\n===== ANALISIS STRUKTUR TREE UIN SUSKA =====")
    print("Jenis struktur       : General Tree")
    print("Root                 : UIN Sultan Syarif Kasim Riau")
    print("Jumlah node          :", tree.count_nodes())
    print("Tinggi               :", tree.height(), "edge")
    print("Jumlah level         :", tree.height() + 1 if tree.root else 0)
    print("Jumlah anak terbanyak:", tree.max_children())
    print("Jumlah node per level:")
    for level, jumlah in enumerate(level_counts):
        print(f"  Level {level}: {jumlah} node")
    print("\nBentuk Tree:")
    print("Bentuk Tree lebar, tetapi tidak seimbang sempurna.")
    print("Sebagian besar cabang berhenti lebih awal, sedangkan cabang FST lebih dalam:")
    print("UIN -> Organ Pengelola -> Rektor -> Dekan FST -> Ketua Prodi TI -> Dosen.")
    print("Tree tidak condong total seperti rantai, beberapa cabang tetap sejajar.")
    print("Tree tidak memiliki aturan pengurutan seperti Binary Search Tree.")
    print("Karena itu, pencarian nama/jabatan tetap O(n) pada kasus terburuk.")


def jalankan_contoh_dosen():
    tree = create_dosen_example_tree()
    print("\n===== CONTOH TERPISAH (18 NODE) =====")
    tampilkan_struktur(tree.root)
    print("Jumlah node:", tree.count_nodes())
    print("Tinggi tree:", tree.height(), "edge")
    print("Jumlah level:", tree.height() + 1)
    tampilkan_hasil_traversal("PREORDER CONTOH Soal", tree.preorder_traversal())
    tampilkan_hasil_traversal("INORDER ADAPTASI CONTOH Soal", tree.inorder_traversal())
    tampilkan_hasil_traversal("POSTORDER CONTOH Soal", tree.postorder_traversal())


def main():
    tree = create_organization_tree()
    print("Data model organisasi UIN Suska Riau berhasil dimuat.")
    print("Jumlah awal node:", tree.count_nodes())
    print("Catatan: ini purwarupa ringkas; nama pimpinan yang tidak diisi memakai placeholder.")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            print("\n===== STRUKTUR ORGANISASI UIN SUSKA RIAU =====")
            tampilkan_struktur(tree.root)
        elif pilihan == "2":
            print("\n===== TAMBAH UNIT / PEGAWAI / JABATAN =====")
            id_node = input("ID baru: ").strip()
            nama = input("Nama atau nama unit: ").strip()
            jabatan = input("Jabatan atau jenis unit: ").strip()
            id_atasan = input("ID parent/atasan: ").strip()
            berhasil = tree.insert_node(id_atasan, TreeNode(id_node, nama, jabatan))
            print("Data berhasil ditambahkan." if berhasil else "Gagal. Periksa ID, data, dan ID parent.")
        elif pilihan == "3":
            kata_kunci = input("Masukkan nama atau jabatan yang dicari: ").strip()
            hasil = tree.search_node(kata_kunci)
            if hasil:
                print("Ditemukan", len(hasil), "hasil:")
                for node in hasil:
                    print(node)
            else:
                print("Data tidak ditemukan.")
        elif pilihan == "4":
            tampilkan_hasil_traversal("PREORDER TRAVERSAL", tree.preorder_traversal())
        elif pilihan == "5":
            tampilkan_hasil_traversal("INORDER TRAVERSAL (ADAPTASI GENERAL TREE)", tree.inorder_traversal())
        elif pilihan == "6":
            tampilkan_hasil_traversal("POSTORDER TRAVERSAL", tree.postorder_traversal())
        elif pilihan == "7":
            tampilkan_analisis(tree)
        elif pilihan == "8":
            jalankan_contoh_dosen()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()
