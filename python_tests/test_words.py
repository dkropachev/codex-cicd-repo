import unittest

from python_pkg.words import reverse_words


class WordTests(unittest.TestCase):
    def test_reverses_words(self):
        self.assertEqual(reverse_words("hello codex"), "codex hello")


if __name__ == "__main__":
    unittest.main()
