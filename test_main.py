import unittest
from main import *

class Test(unittest.TestCase):
    def test_year_format(self):
        self.assertEqual("1991", format_year("1991", "long"))
        self.assertEqual("91", format_year("1991", "short"))
        self.assertEqual("80", format_year("2080", "short"))
        self.assertEqual("", format_year("2080", "none"))

    def test_month_format(self):
        self.assertEqual("October", format_month("October", "long"))
        self.assertEqual("Oct", format_month("October", "short"))
        self.assertEqual("10", format_month("October", "numeric"))
        self.assertEqual("", format_month("October", "none"))
        self.assertEqual("July", format_month("July", "long"))
        self.assertEqual("Jul", format_month("July", "short"))
        self.assertEqual("7", format_month("July", "numeric"))
        self.assertEqual("January", format_month("January", "long"))
        self.assertEqual("Jan", format_month("January", "short"))
        self.assertEqual("1", format_month("January", "numeric"))

    def test_day_format(self):
        self.assertEqual("22nd", format_day("22", "ordinal"))
        self.assertEqual("22", format_day("22", "numeric"))
        self.assertEqual("", format_day("22", "none"))
        self.assertEqual("31st", format_day("31", "ordinal"))
        self.assertEqual("3rd", format_day("3", "ordinal"))
        self.assertEqual("10th", format_day("10", "ordinal"))
        self.assertEqual("9th", format_day("9", "ordinal"))

    def test_format_date(self):
        self.assertEqual("20th October 1999", format_date(year="1999",
            month="October", day="20"))
        self.assertEqual("20/10/99", format_date(year="1999", month="October",
            day="20", day_specifier="numeric", year_specifier="short",
            month_specifier="numeric", separator="/"))
        self.assertEqual("20-Oct-1999", format_date(year="1999",
            month="October", day="20", separator="-", day_specifier="numeric",
            month_specifier="short"))

if __name__ == "__main__":
    unittest.main()
