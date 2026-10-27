
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_file = Path(__file__).parent / "index.html"
        cls.parser = FormParser()

        with html_file.open(encoding="utf-8") as file:
            cls.parser.feed(file.read())

    def test_form_exists(self):
        self.assertTrue(
            any(f.get("id") == "contactForm"
                for f in self.parser.forms),
            "Contact form not found"
        )

    def test_name_field(self):
        self.assertTrue(
            any(i.get("name") == "name"
                and i.get("type") == "text"
                and "required" in i
                for i in self.parser.inputs),
            "Required Name field not found"
        )

    def test_email_field(self):
        self.assertTrue(
            any(i.get("name") == "email"
                and i.get("type") == "email"
                and "required" in i
                for i in self.parser.inputs),
            "Required Email field not found"
        )

    def test_contact_number_field(self):
        self.assertTrue(
            any(i.get("name") == "contact"
                and i.get("type") == "tel"
                and "required" in i
                for i in self.parser.inputs),
            "Required Contact Number field not found"
        )

    def test_submit_button(self):
        self.assertTrue(
            any(b.get("type") == "submit"
                for b in self.parser.buttons),
            "Submit button not found"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
