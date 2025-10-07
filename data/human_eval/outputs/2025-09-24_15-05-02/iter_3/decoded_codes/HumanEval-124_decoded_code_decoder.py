def valid_date(date: str) -> bool:
    """
    Validates if the provided date string is in the format 'MM-DD-YYYY'
    and corresponds to a valid calendar date based on month and day ranges.
    """
    try:
        date = date.strip()
        month_str, day_str, year_str = date.split('-')
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)

        if month < 1 or month > 12:
            return False

        # Months with 31 days
        if month in {1, 3, 5, 7, 8, 10, 12}:
            if day < 1 or day > 31:
                return False

        # Months with 30 days
        elif month in {4, 6, 9, 11}:
            if day < 1 or day > 30:
                return False

        # February (allowing up to 29 regardless of leap year)
        elif month == 2:
            if day < 1 or day > 29:
                return False

        else:
            # This condition is technically unreachable but kept for clarity
            return False

    except Exception:
        return False

    return True