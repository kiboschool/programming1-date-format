# Write your date formatting functions here
# Helper function to format the year
def format_year(year, specifier):
    if specifier == "long":
        return year
    elif specifier == "short":
        return year[-2:]  # last 2 digits
    else:
        return ""


# Helper function to format the month
def format_month(month, specifier):
    if specifier == "long":
        return month
    elif specifier == "short":
        return month[:3]  # first 3 letters
    elif specifier == "numeric":
        months = {
            "January": "1",
            "February": "2",
            "March": "3",
            "April": "4",
            "May": "5",
            "June": "6",
            "July": "7",
            "August": "8",
            "September": "9",
            "October": "10",
            "November": "11",
            "December": "12"
        }
        return months[month]
    else:
        return ""


# Helper function to format the day
def format_day(day, specifier):
    if specifier == "numeric":
        return day
    elif specifier == "ordinal":
        num = int(day)

        # Handle special cases: 10–20
        if 10 <= num % 100 <= 20:
            suffix = "th"
        else:
            last = num % 10
            if last == 1:
                suffix = "st"
            elif last == 2:
                suffix = "nd"
            elif last == 3:
                suffix = "rd"
            else:
                suffix = "th"

        return day + suffix
    else:
        return ""


# Main function that uses the helpers
def format_date(
    year,
    month,
    day,
    year_specifier="long",
    month_specifier="long",
    day_specifier="ordinal",
    separator=" "
):
    # Format each part using helper functions
    y = format_year(year, year_specifier)
    m = format_month(month, month_specifier)
    d = format_day(day, day_specifier)

    # Store parts that are not empty
    parts = []

    if d:
        parts.append(d)
    if m:
        parts.append(m)
    if y:
        parts.append(y)

    # Join parts with the separator
    return separator.join(parts)