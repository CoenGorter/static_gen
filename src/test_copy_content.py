import unittest

from copy_content import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md_header = "# HEADER"
        outcome = extract_title(md_header)
        self.assertEqual(outcome, "HEADER")

    def test_extract_title_with_spaces(self):
        md_header = "# HEADER  "
        outcome = extract_title(md_header)
        self.assertEqual(outcome, "HEADER")

    def test_extract_title_long(self):
        md_header = "# HEADERS AND MORE"
        outcome = extract_title(md_header)
        self.assertEqual(outcome, "HEADERS AND MORE")


if __name__ == "__main__":
    unittest.main()
