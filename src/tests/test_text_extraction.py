import unittest
import sys
import os
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from text_extraction import extract__markdown_images, extract_markdown_links


class TestTextExtraction(unittest.TestCase):
    def test_image_extraction(self) -> None:
        text: str = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result: List[Tuple[str, str]] = extract__markdown_images(text)
        expected_result: List[Tuple[str, str]] = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                                                  ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected_result)

    def test_link_extraction(self) -> None:
        text: str = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result: List[Tuple[str, str]] = extract_markdown_links(text)
        expected_result: List[Tuple[str, str]] = [("to boot dev", "https://www.boot.dev"),
                                                  ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
