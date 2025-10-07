from typing import Any


def valid_date(input_str: str) -> bool:
    try:
        trimmed_str: str = input_str.strip()
        part_a_str, part_b_str, part_c_str = trimmed_str.split('-')
        num_a: int = int(part_a_str)
        num_b: int = int(part_b_str)
        num_c: int = int(part_c_str)

        if not (1 <= num_a <= 12):
            return False

        check_one = num_a in {1, 3, 5, 7, 8, 10, 12}
        cond_one_lower = num_b < 1
        cond_one_upper = num_b > 31
        if check_one and (cond_one_lower or cond_one_upper):
            return False

        check_two = num_a in {4, 6, 9, 11}
        cond_two_lower = num_b < 1
        cond_two_upper = num_b > 30
        if check_two and (cond_two_lower or cond_two_upper):
            return False

        if num_a == 2:
            if num_b < 1 or num_b > 29:
                return False

    except Exception:
        return False

    return True