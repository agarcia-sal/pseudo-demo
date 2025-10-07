from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        clean_date: str = date_string.strip()
        parts_list: list[str] = clean_date.split('-')
        if len(parts_list) != 3:
            return False

        mon: int = int(parts_list[0])
        dy: int = int(parts_list[1])
        yr: int = int(parts_list[2])

        if mon < 1 or mon > 12:
            return False

        if mon in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= dy <= 31):
                return False
        elif mon in {4, 6, 9, 11}:
            if not (1 <= dy <= 30):
                return False
        elif mon == 2:
            if not (1 <= dy <= 29):
                return False
        else:
            return False  # Defensive: should never reach here given mon check above
    except (ValueError, TypeError):
        return False
    return True