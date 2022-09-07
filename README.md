# Date Format

In this exercise, you'll write some helper functions to help with formatting
years, months, and days.

You'll use the helper functions to create a function that can format dates
according to a specification.

## Helper Functions

To build up to the formatter API, you'll write a set of helper functions to
format different parts of the date. Most of them will take in a _format
specifier_ that tells how to 

`format_year`

Takes in a year and a format specifier ('long', 'short', or 'none'). Returns the
year, formatted according to the specifier:

input year: "1999"

long: "1999"
short: "99"
none: ""

`format_month`

Takes in a month and a format specifier ('long', 'short', 'numeric', or 'none').
Returns the month, according to the specifier:

input month: "October"

long: "October"
short: "Oct" (first three letters of the month, for any month)
numeric: "10" 
none: ""

`format_day`

Takes a day of the month and a format specifier ('ordinal', 'numeric', or 'none')
Returns the day of the month, according to the specifier:

input day: "22"
ordinal: "22nd" (ends in '1st' for numbers ending in 1, '2nd' for 2, '3rd' for 3, '4th' '5th' etc for other final digits)
numeric: "22"
none: ""

`format_date`

Takes in a month, day, and year, and optional month, day, and year format
specifiers, as well as an optional separator. Uses the helper functions, and returns a formatted date.

The default specifier options for year, month, and day are 'long', 'long', and 'ordinal'.

The default argument for separator is " ".

Here are some examples of running the `format_date` function:

```python
format_date(year="1999", month="October", day="20") # => "20th October 1999"

format_date("1999", "October", "20", day_specifier="numeric", 
  year_specifier="short", month_specifier="numeric", separator="/") #=> "20/10/99"

format_date("1999", "October", "20", separator="-", day_specifier="numeric", 
  month_specifier="short") #=> "20-Oct-1999"
```

## Testing

As you are developing your solution, test each function on its own. Then, once
you have the whole program completed, test the `format_date` function.

After you've tried things out yourself, run the automated tests to confirm that
your solution is correct.

