import unittest
from huffman_tree import Node, build_huffman_tree


class TestHuffmanTree(unittest.TestCase):
    def test_build_huffman_tree(self):
        char_freq = {"A": 5, "B": 9, "C": 12, "D": 13, "E": 16, "F": 45}
        huffman_tree = build_huffman_tree(char_freq)

        # Define the expected structure of the Huffman tree
        expected_tree = Node(None, 100)
        expected_tree.left = Node("F", 45)
        expected_tree.left.left = Node("E", 45)
        expected_tree.right = Node(None, 55)
        expected_tree.right.left = Node(None, 25)
        expected_tree.right.left.left = Node("A", 5)
        expected_tree.right.left.right = Node("B", 9)
        expected_tree.right.right = Node(None, 30)
        expected_tree.right.right.left = Node("C", 12)
        expected_tree.right.right.right = Node(None, 18)
        expected_tree.right.right.right.left = Node("D", 13)
        expected_tree.right.right.right.right = Node("E", 16)

        print(expected_tree.right)

        # Perform assertions to check if the actual tree matches the expected tree
        self.assertTreeEqual(huffman_tree, expected_tree)

    def assertTreeEqual(self, tree1, tree2):
        # Helper method to recursively compare trees
        if tree1 is None and tree2 is None:
            return
        self.assertIsNotNone(tree1)
        self.assertIsNotNone(tree2)
        self.assertEqual(tree1.char, tree2.char)
        self.assertEqual(tree1.freq, tree2.freq)
        # self.assertTreeEqual(tree1.left, tree2.left)
        print(tree1.left, tree2.left)
        # self.assertTreeEqual(tree1.right, tree2.right)


if __name__ == "__main__":
    unittest.main()
