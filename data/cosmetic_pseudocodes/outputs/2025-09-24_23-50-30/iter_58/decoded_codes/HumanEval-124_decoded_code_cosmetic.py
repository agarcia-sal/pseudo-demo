from typing import Any


def valid_date(a1: str) -> bool:
    try:
        a2 = a1.strip()
        a3, a4, a5 = a2.split('-')
        a6 = int(a3)  # month
        a7 = int(a4)  # day
        a8 = int(a5)  # year, unused in validation

        if a6 < 1 or a6 > 12:
            return False

        # Months with 31 days
        if a6 in {1, 3, 5, 7, 8, 10, 12} and (a7 < 1 or a7 > 31):
            return False

        # Months with 30 days
        if a6 in {4, 6, 9, 11} and (a7 < 1 or a7 > 30):
            return False

        # February with maximum 29 days (leap year not checked)
        if a6 == 2 and (a7 < 1 or a7 > 29):
            return False

    except Exception:
        return False

    return True