import unittest
from main import *

class Test(unittest.TestCase):
    def test_year_format(self):
        self.assertEquals("1991", format_year("1991", "long"))
        self.assertEquals("91", format_year("1991", "short"))
        self.assertEquals("80", format_year("2080", "short"))
        self.assertEquals("", format_year("2080", "none"))

    def test_month_format(self):
        self.assertEquals("October", format_month("October", "long"))
        self.assertEquals("Oct", format_month("October", "short"))
        self.assertEquals("10", format_month("October", "numeric"))
        self.assertEquals("", format_month("October", "none"))
        self.assertEquals("July", format_month("July", "long"))
        self.assertEquals("Jul", format_month("July", "short"))
        self.assertEquals("7", format_month("July", "numeric"))
        self.assertEquals("January", format_month("January", "long"))
        self.assertEquals("Jan", format_month("January", "short"))
        self.assertEquals("1", format_month("January", "numeric"))

    def test_day_format(self):
        self.assertEquals("22nd", format_day("22", "ordinal"))
        self.assertEquals("22", format_day("22", "numeric"))
        self.assertEquals("", format_day("22", "none"))
        self.assertEquals("31st", format_day("31", "ordinal"))
        self.assertEquals("3rd", format_day("3", "ordinal"))
        self.assertEquals("10th", format_day("10", "ordinal"))
        self.assertEquals("9th", format_day("9", "ordinal"))

    def test_format_date(self):
        self.assertEquals("20th October 1999", format_date(year="1999",
            month="October", day="20"))
        self.assertEquals("20/10/99", format_date(year="1999", month="October",
            day="20", day_specifier="numeric", year_specifier="short",
            month_specifier="numeric", separator="/"))
        self.assertEquals("20-Oct-1999", format_date(year="1999",
            month="October", day="20", separator="-", day_specifier="numeric",
            month_specifier="short"))

if __name__ == "__main__":
    unittest.main()
