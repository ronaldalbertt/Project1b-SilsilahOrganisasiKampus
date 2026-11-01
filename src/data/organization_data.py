from src.models.tree_node import TreeNode
from src.models.organization_tree import OrganizationTree


def create_organization_tree():
    # Root menggunakan Dekan karena proyek difokuskan pada struktur internal FST.
    root = TreeNode(
        "ORG001",
        "Nama Dekan (Contoh)",
        "Dekan Fakultas Sains dan Teknologi"
    )

    tree = OrganizationTree(root)

    # Format: ID, Nama, Jabatan, ID Atasan.
    # Judul kelompok "PROGRAM STUDI" dan "LABORATORIUM" pada bagan
    # tidak dibuat sebagai node tersendiri karena bukan kotak jabatan.
    daftar_organisasi = [
        # Wakil Dekan: hubungan langsung di bawah Dekan.
        ("ORG002", "Nama Wakil Dekan I", "Wakil Dekan Bidang Akademik dan Pengembangan Lembaga", "ORG001"),
        ("ORG003", "Nama Wakil Dekan II", "Wakil Dekan Bidang Administrasi Umum, Perencanaan dan Keuangan", "ORG001"),
        ("ORG004", "Nama Wakil Dekan III", "Wakil Dekan Bidang Kemahasiswaan dan Kerjasama", "ORG001"),

        # Kepala Bagian Tata Usaha dan kelompok di bawahnya.
        ("ORG005", "Nama Kepala Bagian Tata Usaha", "Kepala Bagian Tata Usaha", "ORG001"),
        ("ORG006", "Kelompok Jabatan Fungsional dan Pelaksana", "Kelompok Jabatan Fungsional dan Pelaksana", "ORG005"),

        # Program Studi Teknik Informatika.
        ("ORG007", "Program Studi Teknik Informatika", "Program Studi", "ORG001"),
        ("ORG008", "Nama Ketua Prodi TI", "Ketua Prodi Teknik Informatika", "ORG007"),
        ("ORG009", "Nama Sekretaris Prodi TI", "Sekretaris Prodi Teknik Informatika", "ORG007"),

        # Program Studi Teknik Industri.
        ("ORG010", "Program Studi Teknik Industri", "Program Studi", "ORG001"),
        ("ORG011", "Nama Ketua Prodi Teknik Industri", "Ketua Prodi Teknik Industri", "ORG010"),
        ("ORG012", "Nama Sekretaris Prodi Teknik Industri", "Sekretaris Prodi Teknik Industri", "ORG010"),

        # Program Studi Sistem Informasi.
        ("ORG013", "Program Studi Sistem Informasi", "Program Studi", "ORG001"),
        ("ORG014", "Nama Ketua Prodi SI", "Ketua Prodi Sistem Informasi", "ORG013"),
        ("ORG015", "Nama Sekretaris Prodi SI", "Sekretaris Prodi Sistem Informasi", "ORG013"),

        # Program Studi Matematika.
        ("ORG016", "Program Studi Matematika", "Program Studi", "ORG001"),
        ("ORG017", "Nama Ketua Prodi Matematika", "Ketua Prodi Matematika", "ORG016"),
        ("ORG018", "Nama Sekretaris Prodi Matematika", "Sekretaris Prodi Matematika", "ORG016"),

        # Program Studi Teknik Elektro.
        ("ORG019", "Program Studi Teknik Elektro", "Program Studi", "ORG001"),
        ("ORG020", "Nama Ketua Prodi Teknik Elektro", "Ketua Prodi Teknik Elektro", "ORG019"),
        ("ORG021", "Nama Sekretaris Prodi Teknik Elektro", "Sekretaris Prodi Teknik Elektro", "ORG019"),

        # Program Studi Magister Teknik Elektro.
        ("ORG022", "Program Studi Magister Teknik Elektro", "Program Studi", "ORG001"),
        ("ORG023", "Nama Ketua Magister Teknik Elektro", "Ketua Prodi Magister Teknik Elektro", "ORG022"),
        ("ORG024", "Nama Sekretaris Magister Teknik Elektro", "Sekretaris Prodi Magister Teknik Elektro", "ORG022"),

        # Kepala Laboratorium: masing-masing merupakan anak langsung Dekan
        # sesuai pengelompokan pada bagan organisasi yang diberikan.
        ("ORG025", "Nama Kepala Lab Pengembangan Aplikasi", "Kepala Laboratorium Pengembangan Aplikasi", "ORG001"),
        ("ORG026", "Nama Kepala Lab Pengembangan Riset", "Kepala Laboratorium Pengembangan Riset", "ORG001"),
        ("ORG027", "Nama Kepala Lab Teknik Industri", "Kepala Laboratorium Teknik Industri", "ORG001"),
        ("ORG028", "Nama Kepala Lab Sistem Informasi", "Kepala Laboratorium Sistem Informasi", "ORG001"),
        ("ORG029", "Nama Kepala Lab Matematika", "Kepala Laboratorium Matematika", "ORG001"),
        ("ORG030", "Nama Kepala Lab Telekomunikasi dan Elektronika", "Kepala Laboratorium Telekomunikasi dan Elektronika", "ORG001"),
        ("ORG031", "Nama Kepala Lab Komputer dan Energi", "Kepala Laboratorium Komputer dan Energi", "ORG001"),
    ]

    for id_pegawai, nama, jabatan, id_atasan in daftar_organisasi:
        node_baru = TreeNode(id_pegawai, nama, jabatan)
        berhasil = tree.insert_node(id_atasan, node_baru)

        if not berhasil:
            raise ValueError("Gagal memasukkan data: " + id_pegawai)

    return tree
