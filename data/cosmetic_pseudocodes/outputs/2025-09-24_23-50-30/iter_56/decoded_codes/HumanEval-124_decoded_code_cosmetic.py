from typing import Any


def valid_date(input_string: str) -> bool:
    try:
        trimmed_string = input_string.strip()
        parts = trimmed_string.split('-')
        idx_m = int(parts[0])
        idx_d = int(parts[1])
        idx_y = int(parts[2])  # idx_y assigned but unused as per pseudocode

        if idx_m < 1 or idx_m > 12:
            return False

        if idx_m == 2 and (idx_d < 1 or idx_d > 29):
            return False

        if idx_m in {4, 6, 9, 11} and (idx_d < 1 or idx_d > 30):
            return False

        if idx_m in {1, 3, 5, 7, 8, 10, 12} and (idx_d < 1 or idx_d > 31):
            return False

    except Exception:
        return False

    return True