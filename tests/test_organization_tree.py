import unittest

from src.data.organization_data import create_organization_tree
from src.data.traversal_example import create_dosen_example_tree
from src.models.organization_tree import OrganizationTree
from src.models.tree_node import TreeNode


class TestOrganizationTreeUIN(unittest.TestCase):
    def setUp(self):
        self.tree = create_organization_tree()

    def test_root_count_height_and_levels(self):
        self.assertEqual(self.tree.root.id_node, "UIN001")
        self.assertEqual(self.tree.count_nodes(), 27)
        self.assertEqual(self.tree.height(), 5)
        self.assertEqual(self.tree.level_counts(), [1, 3, 4, 17, 1, 1])

    def test_eight_faculties_exist(self):
        faculties = [
            "Fakultas Tarbiyah dan Keguruan",
            "Fakultas Syariah dan Hukum",
            "Fakultas Ushuluddin",
            "Fakultas Dakwah dan Komunikasi",
            "Fakultas Ekonomi dan Sosial",
            "Fakultas Psikologi",
            "Fakultas Sains dan Teknologi",
            "Fakultas Pertanian dan Peternakan",
        ]
        for faculty in faculties:
            self.assertEqual(len(self.tree.search_node(faculty)), 1, faculty)

    def test_separate_governance_groups(self):
        root_ids = [node.id_node for node in self.tree.root.children]
        self.assertEqual(root_ids, ["KAT001", "KAT002", "KAT003"])
        rector = self.tree.search_node("Rektor")[0]
        rector_children = [node.id_node for node in rector.children]
        self.assertIn("ORG002", rector_children)
        self.assertNotIn("ORG019", rector_children)  # Senat bukan bawahan Rektor
        self.assertNotIn("ORG020", rector_children)  # Dewan Pengawas bukan bawahan Rektor
        self.assertNotIn("ORG021", rector_children)  # SPI dipisah sebagai organ pengawas

    def test_fst_prodi_and_dosen_path(self):
        fst = self.tree.search_node("Fakultas Sains dan Teknologi")[0]
        self.assertEqual(fst.children[0].id_node, "PRO001")
        self.assertEqual(fst.children[0].children[0].id_node, "DOS001")

    def test_all_traversals_visit_each_node_once(self):
        expected = self.tree.count_nodes()
        traversals = (
            self.tree.preorder_traversal(),
            self.tree.inorder_traversal(),
            self.tree.postorder_traversal(),
        )
        for result in traversals:
            self.assertEqual(len(result), expected)
            ids = [node.id_node for node in result]
            self.assertEqual(len(ids), len(set(ids)))

    def test_preorder_starts_at_root(self):
        self.assertEqual(self.tree.preorder_traversal()[0].id_node, "UIN001")

    def test_postorder_ends_at_root(self):
        self.assertEqual(self.tree.postorder_traversal()[-1].id_node, "UIN001")

    def test_search_is_case_insensitive_and_partial(self):
        result = self.tree.search_node("TEKNIK INFORMATIKA")
        ids = [node.id_node for node in result]
        self.assertIn("PRO001", ids)
        self.assertIn("DOS001", ids)

    def test_search_blank_returns_empty(self):
        self.assertEqual(self.tree.search_node("   "), [])

    def test_insert_node_success(self):
        node = TreeNode("TEST001", "Nama Contoh", "Staf Contoh")
        self.assertTrue(self.tree.insert_node("ORG002", node))
        self.assertEqual(self.tree.count_nodes(), 28)

    def test_duplicate_id_is_rejected(self):
        node = TreeNode("ORG002", "Nama Duplikat", "Wakil Rektor")
        self.assertFalse(self.tree.insert_node("ORG001", node))
        self.assertEqual(self.tree.count_nodes(), 27)

    def test_unknown_parent_is_rejected(self):
        node = TreeNode("TEST002", "Nama Contoh", "Staf Contoh")
        self.assertFalse(self.tree.insert_node("ID-TIDAK-ADA", node))


class TestLecturerTraversalExample(unittest.TestCase):
    def test_example_has_18_nodes_and_height_5(self):
        tree = create_dosen_example_tree()
        self.assertEqual(tree.count_nodes(), 18)
        self.assertEqual(tree.height(), 5)

    def test_example_postorder_order(self):
        tree = create_dosen_example_tree()
        names = [node.nama for node in tree.postorder_traversal()]
        self.assertEqual(names, [
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
            "Dosen Pengampu Mata Kuliah",
            "Koordinator Dosen",
            "Ketua Program Studi Teknik Informatika",
            "Dekan Fakultas Sains dan Teknologi",
            "Rektor",
        ])


if __name__ == "__main__":
    unittest.main()
