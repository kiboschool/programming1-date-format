# Write your date formatting functions here

def format_year(year, specifier):
    if specifier == "long":
        return year
    elif specifier == "short":
        return year[-2:]
    elif specifier == "none":
        return ""

def format_month(month, specifier):
    if specifier == "long":
        return month
    elif specifier == "short":
        return month[0:3]
    elif specifier == "numeric":
        index = ["January", "February", "March",
                "April", "May", "June", "July",
                "August", "September", "October", 
                "November", "December"].index(month)
        return str(index + 1)
    elif specifier == "none":
        return ""

def format_day(day, specifier):
    if specifier == "ordinal":
        last_digit = day[-1]
        if last_digit == "1":
            return day + "st"
        elif last_digit == "2":
            return day + "nd"
        elif last_digit == "3":
            return day + "rd"
        else:
            return day + "th"
    elif specifier == "numeric":
        return day
    elif specifier == "none":
        return ""

def format_date(year, month, day, year_specifier="long", month_specifier="long",
        day_specifier="ordinal", separator=" "):
    return separator.join([
        format_day(day, day_specifier),
        format_month(month, month_specifier),
        format_year(year, year_specifier)
        ])
