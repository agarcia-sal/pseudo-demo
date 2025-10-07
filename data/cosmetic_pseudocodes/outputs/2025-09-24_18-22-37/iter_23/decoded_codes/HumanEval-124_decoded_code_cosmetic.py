from typing import Any


def valid_date(input_str: str) -> bool:
    try:
        trimmed_input: str = input_str.strip()
        parts: list[str] = trimmed_input.split('-')
        part_month: str = parts[0]
        part_day: str = parts[1]
        part_year: str = parts[2]

        numeric_month: int = int(part_month)
        numeric_day: int = int(part_day)
        numeric_year: int = int(part_year)

        if numeric_month < 1 or numeric_month > 12:
            return False

        if numeric_month in {1, 3, 5, 7, 8, 10, 12}:
            if numeric_day < 1 or numeric_day > 31:
                return False

        elif numeric_month in {4, 6, 9, 11}:
            if numeric_day < 1 or numeric_day > 30:
                return False

        elif numeric_month == 2:
            max_day_feb: int = 29
            if numeric_day < 1 or numeric_day > max_day_feb:
                return False

        else:
            # Defensive fallback, should not occur due to earlier month range check
            return False

    except Exception:
        return False

    return True