import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')

        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode('This is a text node', 'bold', None)
        node2 = TextNode('This is a text node', 'bold',
                        'https://lucasamachado.com')
        
        self.assertNotEqual(node, node2)

    def test_not_eq_all(self):
        node = TextNode('This is a text node.', 'bold.', "https://lucasamachado.com/test")
        node2 = TextNode('This is a text node', 'bold',
                        'https://lucasamachado.com')
        
        self.assertNotEqual(node, node2) 


if __name__ == "__main__":
    unittest.main()
