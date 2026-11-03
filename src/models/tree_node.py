
class TreeNode:

    def __init__(self, id_node, nama, jabatan):
        self.id_node = id_node
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def __str__(self):
        return (
            f"ID: {self.id_node} | "
            f"Nama/Unit: {self.nama} | "
            f"Jabatan/Jenis: {self.jabatan}"
        )
