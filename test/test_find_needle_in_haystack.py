import unittest
from src.find_needle_in_haystack import knuth_morris_pratt, prefix_function


class TestKMP(unittest.TestCase):
    def test_knuth_morris_pratt_found(self):
        needle = "pupulup"
        haystack = "gxfgplpulupupluupupulup"
        self.assertEqual(knuth_morris_pratt(needle, haystack), [16])

    def test_knuth_morris_pratt_not_found(self):
        needle = "bep"
        haystack = "gxfgplpulupupluupupulup"
        self.assertEqual(knuth_morris_pratt(needle, haystack), [])

    def test_kmp_search_empty_needle(self):
        needle = ""
        haystack = "gxfgplpulupupluupupulup"
        self.assertFalse(needle, haystack)

    def test_kmp_search_empty_haystack(self):
        needle = "bep"
        haystack = ""
        self.assertEqual(knuth_morris_pratt(needle, haystack), [])

    def test_kmp_search_both_empty(self):
        needle = ""
        haystack = ""
        self.assertFalse(knuth_morris_pratt(needle, haystack))


class TestPrefixFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(prefix_function(""), "no needle")

    def test_single_character_string(self):
        self.assertEqual(prefix_function("bab"), [0, 0, 1])

    def test_repeating_characters(self):
        self.assertEqual(prefix_function("bbb"), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
