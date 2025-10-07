import unittest
from src.data.products import products

class TestProducts(unittest.TestCase):

    def test_product_mapping(self):
        self.assertIn('CNO Financial Group', products)
        self.assertIsInstance(products['CNO Financial Group'], dict)

    def test_product_categories(self):
        categories = products['CNO Financial Group']
        self.assertIn('Life Insurance', categories)
        self.assertIn('Health Insurance', categories)
        self.assertIn('Annuities', categories)

    def test_product_accessibility(self):
        categories = products['CNO Financial Group']
        self.assertIsInstance(categories['Life Insurance'], list)
        self.assertIsInstance(categories['Health Insurance'], list)
        self.assertIsInstance(categories['Annuities'], list)

if __name__ == '__main__':
    unittest.main()