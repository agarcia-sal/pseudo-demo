from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input = date_string.strip()
        parts = trimmed_input.split('-')
        if len(parts) != 3:
            return False
        str_m, str_d, str_y = parts
        mth = int(str_m)
        dy = int(str_d)
        yr = int(str_y)

        if not (1 <= mth <= 12):
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
        else:
            return False  # Should not be reached given previous checks

    except Exception:
        return False

    return True