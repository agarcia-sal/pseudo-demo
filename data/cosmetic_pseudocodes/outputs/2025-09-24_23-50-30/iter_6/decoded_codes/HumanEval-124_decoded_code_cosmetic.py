from typing import List


def valid_date(date_input: str) -> bool:
    trimmed_input: str = date_input.strip()
    parts: List[str] = trimmed_input.split('-')
    if len(parts) != 3:
        return False

    try:
        num_m: int = int(parts[0])
        num_d: int = int(parts[1])
        num_y: int = int(parts[2])
    except ValueError:
        return False

    if num_m < 1 or num_m > 12:
        return False

    months_with_31: List[int] = [1, 3, 5, 7, 8, 10, 12]
    months_with_30: List[int] = [4, 6, 9, 11]

    if num_m in months_with_31:
        if num_d < 1 or num_d > 31:
            return False
    elif num_m in months_with_30:
        if num_d < 1 or num_d > 30:
            return False
    else:
        if num_d < 1 or num_d > 29:
            return False

    return True