import unittest
from paquete.app import App

class TestBasic(unittest.TestCase):

    def setUp(self):
        self.app = App()

    def test_app_run(self):
        result = self.app.run()
        self.assertEqual(result, "Expected Output")  # Replace with actual expected output

if __name__ == '__main__':
    unittest.main()