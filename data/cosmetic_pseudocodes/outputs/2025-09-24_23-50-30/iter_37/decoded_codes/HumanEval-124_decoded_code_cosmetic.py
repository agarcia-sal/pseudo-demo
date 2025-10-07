from typing import Optional


def valid_date(input_string: str) -> bool:
    try:
        trimmed_input = input_string.strip()
        parts = trimmed_input.split('-')
        first_part = parts[0]
        second_part = parts[1]
        third_part = parts[2]

        m = int(first_part)
        d = int(second_part)
        y = int(third_part)

        if (m < 1) or (m > 12):
            return False
        if (m in {1, 3, 5, 7, 8, 10, 12}) and ((d < 1) or (d > 31)):
            return False
        if (m in {4, 6, 9, 11}) and ((d < 1) or (d > 30)):
            return False
        if (m == 2) and ((d < 1) or (d > 29)):
            return False
    except Exception:
        return False

    return True