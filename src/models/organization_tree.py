from src.models.tree_node import TreeNode


class OrganizationTree:
    def __init__(self, root=None):
        self.root = root

    def _search_by_id(self, current, id_pegawai):
        if current is None:
            return None

        if current.id_pegawai == id_pegawai:
            return current

        for child in current.children:
            hasil = self._search_by_id(child, id_pegawai)

            if hasil is not None:
                return hasil

        return None

    def insert_node(self, id_atasan, node):
        if self.root is None:
            return False

        if not isinstance(node, TreeNode):
            return False

        if not isinstance(id_atasan, str) or id_atasan.strip() == "":
            return False

        if (
            not isinstance(node.id_pegawai, str)
            or node.id_pegawai.strip() == ""
            or not isinstance(node.nama, str)
            or node.nama.strip() == ""
            or not isinstance(node.jabatan, str)
            or node.jabatan.strip() == ""
        ):
            return False

        if self._search_by_id(self.root, node.id_pegawai) is not None:
            return False

        atasan = self._search_by_id(self.root, id_atasan)

        if atasan is None:
            return False

        atasan.children.append(node)
        return True

    def search_node(self, kata_kunci):
        hasil = []

        if (
            self.root is None
            or not isinstance(kata_kunci, str)
            or kata_kunci.strip() == ""
        ):
            return hasil

        self._search_by_keyword(self.root, kata_kunci.lower(), hasil)
        return hasil

    def _search_by_keyword(self, current, kata_kunci, hasil):
        if (
            kata_kunci in current.nama.lower()
            or kata_kunci in current.jabatan.lower()
        ):
            hasil.append(current)

        for child in current.children:
            self._search_by_keyword(child, kata_kunci, hasil)

    # PREORDER: node saat ini, kemudian seluruh subtree anak.
    def preorder_traversal(self):
        hasil = []

        if self.root is not None:
            self._preorder(self.root, hasil)

        return hasil

    def _preorder(self, current, hasil):
        hasil.append(current)

        for child in current.children:
            self._preorder(child, hasil)

    # INORDER ADAPTASI GENERAL TREE:
    # subtree anak pertama, node saat ini, lalu subtree anak berikutnya.
    def inorder_traversal(self):
        hasil = []

        if self.root is not None:
            self._inorder(self.root, hasil)

        return hasil

    def _inorder(self, current, hasil):
        if len(current.children) > 0:
            self._inorder(current.children[0], hasil)

        hasil.append(current)

        for child in current.children[1:]:
            self._inorder(child, hasil)

    # POSTORDER: seluruh subtree anak, kemudian node saat ini.
    def postorder_traversal(self):
        hasil = []

        if self.root is not None:
            self._postorder(self.root, hasil)

        return hasil

    def _postorder(self, current, hasil):
        for child in current.children:
            self._postorder(child, hasil)

        hasil.append(current)

    def count_nodes(self):
        if self.root is None:
            return 0

        return self._count_nodes(self.root)

    def _count_nodes(self, current):
        jumlah = 1

        for child in current.children:
            jumlah += self._count_nodes(child)

        return jumlah

    def height(self):
        if self.root is None:
            return -1

        return self._height(self.root)

    def _height(self, current):
        tinggi_maks = 0

        for child in current.children:
            tinggi_anak = self._height(child)

            if tinggi_anak > tinggi_maks:
                tinggi_maks = tinggi_anak

        if len(current.children) == 0:
            return 0

        return tinggi_maks + 1
