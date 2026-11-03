
from src.models.tree_node import TreeNode
from src.models.organization_tree import OrganizationTree


def create_organization_tree():

    # Root utama UIN Sultan Syarif Kasim Riau.
    root = TreeNode(
        "UIN001",
        "UIN Sultan Syarif Kasim Riau",
        "Institusi / Root"
    )

    tree = OrganizationTree(root)

    # Format: ID, Nama/Unit, Jabatan/Jenis, ID Atasan.
    # Semua nama individu dalam data ini merupakan nama fiktif untuk contoh.

    daftar_organisasi = [

        # Tiga kelompok organisasi.
        ("KAT001", "Bagian Pengelola / Pimpinan Universitas", "Kelompok Organisasi", "UIN001"),
        ("KAT002", "Bagian Pertimbangan", "Kelompok Organisasi", "UIN001"),
        ("KAT003", "Bagian Pengawas", "Kelompok Organisasi", "UIN001"),

        # Pimpinan universitas.
        ("ORG001", "Arif Pratama (Contoh)", "Rektor", "KAT001"),
        ("ORG002", "Siti Rahmawati (Contoh)", "Wakil Rektor I", "ORG001"),
        ("ORG003", "Budi Santoso (Contoh)", "Wakil Rektor II", "ORG001"),
        ("ORG004", "Nur Aisyah (Contoh)", "Wakil Rektor III", "ORG001"),

        # Delapan fakultas.
        ("FAK001", "Ahmad Fauzan (Contoh)", "Dekan Fakultas Tarbiyah dan Keguruan", "ORG001"),
        ("FAK002", "Rina Safitri (Contoh)", "Dekan Fakultas Syariah dan Hukum", "ORG001"),
        ("FAK003", "Muhammad Ilham (Contoh)", "Dekan Fakultas Ushuluddin", "ORG001"),
        ("FAK004", "Dedi Kurniawan (Contoh)", "Dekan Fakultas Dakwah dan Komunikasi", "ORG001"),
        ("FAK005", "Lina Marlina (Contoh)", "Dekan Fakultas Ekonomi dan Sosial", "ORG001"),
        ("FAK006", "Putri Ananda (Contoh)", "Dekan Fakultas Psikologi", "ORG001"),
        ("FAK007", "Fajar Ramadhan (Contoh)", "Dekan Fakultas Sains dan Teknologi", "ORG001"),
        ("FAK008", "Eko Saputra (Contoh)", "Dekan Fakultas Pertanian dan Peternakan", "ORG001"),

        # Pascasarjana dan unit universitas.
        ("PAS001", "Yuli Astuti (Contoh)", "Direktur Pascasarjana", "ORG001"),
        ("BRI001", "Rizky Firmansyah (Contoh)", "Kepala Biro AUPK", "ORG001"),
        ("BRI002", "Dewi Lestari (Contoh)", "Kepala Biro AAKK", "ORG001"),
        ("LEM001", "Bambang Hidayat (Contoh)", "Ketua LPPM", "ORG001"),
        ("LEM002", "Nanda Permata (Contoh)", "Ketua LPM", "ORG001"),
        ("UPT001", "Rudi Hartono (Contoh)", "Kepala PTIPD", "ORG001"),

        # Organ pertimbangan.
        ("ORG019", "Senat Universitas", "Organ Pertimbangan", "KAT002"),
        ("ORG020", "Dewan Pengawas", "Organ Pertimbangan", "KAT002"),

        # Organ pengawas.
        ("ORG021", "Satuan Pengawas Internal", "Organ Pengawas (SPI)", "KAT003"),

        # Contoh hierarki fakultas sampai dosen.
        ("PRO001", "Muhammad Affandes S.T M.T", "Ketua Prodi Teknik Informatika", "FAK007"),
        ("DOS001", "Maya Putri (Contoh)", "Dosen Teknik Informatika", "PRO001"),
    ]

    for id_node, nama, jabatan, id_atasan in daftar_organisasi:

        node_baru = TreeNode(id_node, nama, jabatan)

        if not tree.insert_node(id_atasan, node_baru):
            raise ValueError(
                f"Gagal memasukkan data organisasi: {id_node}"
            )

    if tree.count_nodes() != 27:
        raise ValueError(
            f"Jumlah node tidak sesuai. Ditemukan: {tree.count_nodes()}"
        )

    return tree
