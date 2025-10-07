from typing import Optional


def valid_date(input_str: str) -> bool:
    try:
        trimmed_str = input_str.strip()
        first_part, second_part, third_part = trimmed_str.split('-')
        mth = int(first_part)
        dy = int(second_part)
        yr = int(third_part)

        if mth < 1 or mth > 12:
            return False
        if mth in {1, 3, 5, 7, 8, 10, 12}:
            if dy < 1 or dy > 31:
                return False
        elif mth in {4, 6, 9, 11}:
            if dy < 1 or dy > 30:
                return False
        elif mth == 2:
            if dy < 1 or dy > 29:
                return False
    except Exception:
        return False

    return True