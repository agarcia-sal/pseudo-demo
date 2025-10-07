from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input: str = date_string.strip()
        parts: list[str] = trimmed_input.split('-')
        month_component: str = parts[0]
        day_component: str = parts[1]
        year_component: str = parts[2]

        month_num: int = int(month_component)
        day_num: int = int(day_component)
        year_num: int = int(year_component)

        if not (1 <= month_num <= 12):
            return False

        if month_num == 2:
            if day_num < 1 or day_num > 29:
                return False
        else:
            if month_num in {1, 3, 5, 7, 8, 10, 12}:
                if day_num < 1 or day_num > 31:
                    return False
            elif month_num in {4, 6, 9, 11}:
                if day_num < 1 or day_num > 30:
                    return False
            else:
                return False

    except Exception:  # covers all exceptions raised during parsing/conversion/indexing
        return False

    return True