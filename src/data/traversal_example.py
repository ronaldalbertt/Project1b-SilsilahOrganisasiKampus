from src.models.tree_node import TreeNode
from src.models.organization_tree import OrganizationTree


def create_dosen_example_tree():
    """
    Membuat struktur 18 node sesuai contoh traversal pada lembar aktivitas dosen.
    Data ini terpisah dari data utama organisasi FST.
    """
    root = TreeNode("DOS001", "Rektor", "Rektor")
    tree = OrganizationTree(root)

    # Format: ID, Nama, Jabatan, ID Atasan.
    daftar = [
        ("DOS002", "Senat Universitas", "Senat Universitas", "DOS001"),
        ("DOS003", "Wakil Rektor I", "Wakil Rektor I (Bidang Akademik)", "DOS001"),
        ("DOS004", "Wakil Rektor II", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)", "DOS001"),
        ("DOS005", "Wakil Rektor III", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)", "DOS001"),

        ("DOS006", "Dekan Fakultas Sains dan Teknologi", "Dekan Fakultas Sains dan Teknologi", "DOS001"),
        ("DOS007", "Wakil Dekan I", "Wakil Dekan I (Bidang Akademik & Kelembagaan)", "DOS006"),
        ("DOS008", "Wakil Dekan II", "Wakil Dekan II (Bidang AUPK)", "DOS006"),
        ("DOS009", "Wakil Dekan III", "Wakil Dekan III (Bidang Kemahasiswaan)", "DOS006"),

        ("DOS010", "Ketua Program Studi Teknik Informatika", "Ketua Program Studi Teknik Informatika", "DOS006"),
        ("DOS011", "Sekretaris Program Studi", "Sekretaris Program Studi", "DOS010"),
        ("DOS012", "Kepala Laboratorium Komputer", "Kepala Laboratorium Komputer", "DOS010"),
        ("DOS013", "Asisten Laboratorium", "Asisten Laboratorium", "DOS012"),
        ("DOS014", "Teknisi Laboratorium", "Teknisi Laboratorium", "DOS012"),

        ("DOS015", "Koordinator Dosen", "Koordinator Dosen", "DOS010"),
        ("DOS016", "Dosen Pembimbing Akademik", "Dosen Pembimbing Akademik", "DOS015"),
        ("DOS017", "Mahasiswa Bimbingan", "Mahasiswa Bimbingan (Leaf)", "DOS016"),
        ("DOS018", "Dosen Pengampu Mata Kuliah", "Dosen Pengampu Mata Kuliah", "DOS015"),
    ]

    for id_node, nama, jabatan, id_atasan in daftar:
        node_baru = TreeNode(id_node, nama, jabatan)

        if not tree.insert_node(id_atasan, node_baru):
            raise ValueError("Gagal memasukkan contoh node: " + id_node)

    return tree
