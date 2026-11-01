# Class Diagram Proyek 1b

Diagram berikut menggambarkan class yang digunakan pada implementasi Python.

```mermaid
classDiagram
    class TreeNode {
        +id_pegawai
        +nama
        +jabatan
        +children: List[TreeNode]
        +__init__(id_pegawai, nama, jabatan)
        +__str__()
    }

    class OrganizationTree {
        -root: TreeNode
        +__init__(root=None)
        +insert_node(id_atasan, node)
        +search_node(kata_kunci)
        +preorder_traversal()
        +inorder_traversal()
        +postorder_traversal()
        +count_nodes()
        +height()
        -_search_by_id(current, id_pegawai)
        -_search_by_keyword(current, kata_kunci, hasil)
        -_preorder(current, hasil)
        -_inorder(current, hasil)
        -_postorder(current, hasil)
        -_count_nodes(current)
        -_height(current)
    }

    OrganizationTree "1" *-- "1" TreeNode : root
    TreeNode "1" *-- "0..*" TreeNode : children
```

Keterangan: tanda `+` menunjukkan method/atribut publik dan tanda `-` menunjukkan bagian internal (helper/private) pada rancangan. Satu `OrganizationTree` memiliki satu root, sedangkan setiap `TreeNode` dapat memiliki nol atau lebih child.
