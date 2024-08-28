import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        """Test that the title is correctly extracted from valid markdown."""
        markdown = "# Sample Title\n\nSome other content."
        expected_title = "Sample Title"
        result = extract_title(markdown)
        self.assertEqual(result, expected_title)

    def test_extract_title_no_h1(self):
        """Test that an exception is raised when no H1 title is present."""
        markdown = "## Sample Subtitle\n\nSome other content."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Must have an h1 title")

    def test_extract_title_multiple_hashes(self):
        """Test that an exception is raised when multiple '#' are present in the title."""
        markdown = "### Sample Title\n\nSome other content."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Must have an h1 title")

    def test_extract_title_empty_markdown(self):
        """Test that an exception is raised when markdown is empty."""
        markdown = ""
        with self.assertRaises(IndexError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
