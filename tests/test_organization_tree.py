import unittest

from src.data.organization_data import create_organization_tree
from src.models.tree_node import TreeNode
from src.models.organization_tree import OrganizationTree
from src.data.traversal_example import create_dosen_example_tree


class TestOrganizationTree(unittest.TestCase):
    def setUp(self):
        self.tree = create_organization_tree()

    def test_initial_node_count_and_height(self):
        self.assertEqual(self.tree.count_nodes(), 31)
        self.assertEqual(self.tree.height(), 2)

    def test_all_traversals_visit_every_node_once(self):
        expected_count = self.tree.count_nodes()
        for hasil in (
            self.tree.preorder_traversal(),
            self.tree.inorder_traversal(),
            self.tree.postorder_traversal(),
        ):
            self.assertEqual(len(hasil), expected_count)
            ids = [node.id_pegawai for node in hasil]
            self.assertEqual(len(ids), len(set(ids)))

    def test_preorder_starts_with_root(self):
        self.assertEqual(self.tree.preorder_traversal()[0].id_pegawai, "ORG001")

    def test_postorder_ends_with_root(self):
        self.assertEqual(self.tree.postorder_traversal()[-1].id_pegawai, "ORG001")

    def test_search_is_case_insensitive_and_partial(self):
        hasil = self.tree.search_node("teknik informatika")
        ids = [node.id_pegawai for node in hasil]
        self.assertIn("ORG007", ids)
        self.assertIn("ORG008", ids)
        self.assertIn("ORG009", ids)

    def test_search_empty_keyword_returns_empty_list(self):
        self.assertEqual(self.tree.search_node("   "), [])

    def test_insert_node_success(self):
        node = TreeNode("TEST001", "Nama Contoh", "Staf Contoh")
        self.assertTrue(self.tree.insert_node("ORG002", node))
        self.assertEqual(self.tree.count_nodes(), 32)

    def test_insert_duplicate_id_is_rejected(self):
        node = TreeNode("ORG002", "Nama Duplikat", "Jabatan Contoh")
        self.assertFalse(self.tree.insert_node("ORG001", node))
        self.assertEqual(self.tree.count_nodes(), 31)

    def test_insert_with_unknown_parent_is_rejected(self):
        node = TreeNode("TEST002", "Nama Contoh", "Staf Contoh")
        self.assertFalse(self.tree.insert_node("TIDAK-ADA", node))

    def test_insert_empty_fields_is_rejected(self):
        node = TreeNode(" ", "Nama Contoh", "Staf Contoh")
        self.assertFalse(self.tree.insert_node("ORG001", node))

    def test_dosen_example_has_expected_node_count_and_height(self):
        tree = create_dosen_example_tree()
        self.assertEqual(tree.count_nodes(), 18)
        self.assertEqual(tree.height(), 5)

    def test_dosen_example_preorder_order(self):
        tree = create_dosen_example_tree()
        hasil = [node.nama for node in tree.preorder_traversal()]
        self.assertEqual(hasil, [
            "Rektor",
            "Senat Universitas",
            "Wakil Rektor I",
            "Wakil Rektor II",
            "Wakil Rektor III",
            "Dekan Fakultas Sains dan Teknologi",
            "Wakil Dekan I",
            "Wakil Dekan II",
            "Wakil Dekan III",
            "Ketua Program Studi Teknik Informatika",
            "Sekretaris Program Studi",
            "Kepala Laboratorium Komputer",
            "Asisten Laboratorium",
            "Teknisi Laboratorium",
            "Koordinator Dosen",
            "Dosen Pembimbing Akademik",
            "Mahasiswa Bimbingan",
            "Dosen Pengampu Mata Kuliah",
        ])

    def test_dosen_example_inorder_order(self):
        tree = create_dosen_example_tree()
        hasil = [node.nama for node in tree.inorder_traversal()]
        self.assertEqual(hasil, [
            "Senat Universitas",
            "Rektor",
            "Wakil Rektor I",
            "Wakil Rektor II",
            "Wakil Rektor III",
            "Wakil Dekan I",
            "Dekan Fakultas Sains dan Teknologi",
            "Wakil Dekan II",
            "Wakil Dekan III",
            "Sekretaris Program Studi",
            "Ketua Program Studi Teknik Informatika",
            "Asisten Laboratorium",
            "Kepala Laboratorium Komputer",
            "Teknisi Laboratorium",
            "Mahasiswa Bimbingan",
            "Dosen Pembimbing Akademik",
            "Koordinator Dosen",
            "Dosen Pengampu Mata Kuliah",
        ])

    def test_dosen_example_postorder_order(self):
        tree = create_dosen_example_tree()
        hasil = [node.nama for node in tree.postorder_traversal()]
        self.assertEqual(hasil, [
            "Senat Universitas",
            "Wakil Rektor I",
            "Wakil Rektor II",
            "Wakil Rektor III",
            "Wakil Dekan I",
            "Wakil Dekan II",
            "Wakil Dekan III",
            "Sekretaris Program Studi",
            "Asisten Laboratorium",
            "Teknisi Laboratorium",
            "Kepala Laboratorium Komputer",
            "Mahasiswa Bimbingan",
            "Dosen Pembimbing Akademik",
            "Koordinator Dosen",
            "Dosen Pengampu Mata Kuliah",
            "Ketua Program Studi Teknik Informatika",
            "Dekan Fakultas Sains dan Teknologi",
            "Rektor",
        ])

    def test_traversal_order_on_small_tree(self):
        root = TreeNode("A", "Root", "Root")
        tree = OrganizationTree(root)
        node_b = TreeNode("B", "B", "B")
        node_c = TreeNode("C", "C", "C")
        node_d = TreeNode("D", "D", "D")
        node_e = TreeNode("E", "E", "E")
        self.assertTrue(tree.insert_node("A", node_b))
        self.assertTrue(tree.insert_node("A", node_c))
        self.assertTrue(tree.insert_node("B", node_d))
        self.assertTrue(tree.insert_node("C", node_e))

        preorder = [node.id_pegawai for node in tree.preorder_traversal()]
        inorder = [node.id_pegawai for node in tree.inorder_traversal()]
        postorder = [node.id_pegawai for node in tree.postorder_traversal()]

        self.assertEqual(preorder, ["A", "B", "D", "C", "E"])
        self.assertEqual(inorder, ["D", "B", "A", "E", "C"])
        self.assertEqual(postorder, ["D", "B", "E", "C", "A"])


if __name__ == "__main__":
    unittest.main()
