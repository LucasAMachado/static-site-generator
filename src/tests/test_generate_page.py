import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from generate_page import extract_title
import unittest



class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self) -> None:
        """Test that the title is correctly extracted from valid markdown."""
        markdown: str = "# Sample Title\n\nSome other content."
        expected_title: str = "Sample Title"
        result: str = extract_title(markdown)
        self.assertEqual(result, expected_title)

    def test_extract_title_no_h1(self) -> None:
        """Test that an exception is raised when no H1 title is present."""
        markdown: str = "## Sample Subtitle\n\nSome other content."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Must have an h1 title")

    def test_extract_title_multiple_hashes(self) -> None:
        """Test that an exception is raised when multiple '#' are present in the title."""
        markdown: str = "### Sample Title\n\nSome other content."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Must have an h1 title")

    def test_extract_title_empty_markdown(self) -> None:
        """Test that an exception is raised when markdown is empty."""
        markdown: str = ""
        with self.assertRaises(IndexError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
