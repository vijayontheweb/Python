import cap_utils
import unittest


class TestCap(unittest.TestCase):
    def test_title(self):
        word = "vijay anand"
        self.assertEqual(cap_utils.to_title(word), "Vijay Anand")

    def test_caps(self):
        word = "vijay anand"
        self.assertEqual(cap_utils.to_capital(word), "Vijay Anand")


if __name__ == "__main__":
    unittest.main()
