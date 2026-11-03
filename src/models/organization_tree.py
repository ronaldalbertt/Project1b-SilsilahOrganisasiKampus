from src.models.tree_node import TreeNode


class OrganizationTree:
    """General Tree untuk memodelkan hubungan organisasi UIN Suska Riau."""

    def __init__(self, root=None):
        self.root = root

    def _search_by_id(self, current, id_node):
        if current is None:
            return None
        if current.id_node == id_node:
            return current
        for child in current.children:
            hasil = self._search_by_id(child, id_node)
            if hasil is not None:
                return hasil
        return None

    def insert_node(self, id_atasan, node):

        if self.root is None or not isinstance(node, TreeNode):
            return False
        if not isinstance(id_atasan, str) or not id_atasan.strip():
            return False
        for value in (node.id_node, node.nama, node.jabatan):
            if not isinstance(value, str) or not value.strip():
                return False
        if self._search_by_id(self.root, node.id_node) is not None:
            return False
        atasan = self._search_by_id(self.root, id_atasan)
        if atasan is None:
            return False
        atasan.children.append(node)
        return True

    def search_node(self, kata_kunci):
        hasil = []
        if self.root is None or not isinstance(kata_kunci, str) or not kata_kunci.strip():
            return hasil
        self._search_by_keyword(self.root, kata_kunci.strip().casefold(), hasil)
        return hasil

    def _search_by_keyword(self, current, kata_kunci, hasil):
        if kata_kunci in current.nama.casefold() or kata_kunci in current.jabatan.casefold():
            hasil.append(current)
        for child in current.children:
            self._search_by_keyword(child, kata_kunci, hasil)

    def preorder_traversal(self):
        hasil = []
        if self.root is not None:
            self._preorder(self.root, hasil)
        return hasil

    def _preorder(self, current, hasil):
        hasil.append(current)
        for child in current.children:
            self._preorder(child, hasil)

    def inorder_traversal(self):

        hasil = []
        if self.root is not None:
            self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, current, hasil):
        if current.children:
            self._inorder(current.children[0], hasil)
        hasil.append(current)
        for child in current.children[1:]:
            self._inorder(child, hasil)

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
        if not current.children:
            return 0
        return 1 + max(self._height(child) for child in current.children)

    def level_counts(self):
        if self.root is None:
            return []
        counts = []
        queue = [(self.root, 0)]
        index = 0
        while index < len(queue):
            node, level = queue[index]
            index += 1
            while len(counts) <= level:
                counts.append(0)
            counts[level] += 1
            for child in node.children:
                queue.append((child, level + 1))
        return counts

    def max_children(self):
        if self.root is None:
            return 0
        maksimum = 0
        stack = [self.root]
        while stack:
            current = stack.pop()
            maksimum = max(maksimum, len(current.children))
            stack.extend(current.children)
        return maksimum
