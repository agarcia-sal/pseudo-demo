from typing import Optional


def valid_date(input_string: str) -> bool:
    try:
        trimmed_val: str = input_string.strip()
        parts_list: list[str] = trimmed_val.split('-')
        if len(parts_list) != 3:
            return False
        part_one, part_two, part_three = parts_list

        num_one: int = int(part_one)
        num_two: int = int(part_two)
        # num_three is parsed but not used in validation per pseudocode
        _num_three: int = int(part_three)

        if not (1 <= num_one <= 12):
            return False

        if num_one in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= num_two <= 31):
                return False
        elif num_one in {4, 6, 9, 11}:
            if not (1 <= num_two <= 30):
                return False
        elif num_one == 2:
            if not (1 <= num_two <= 29):
                return False
        else:
            # Should not be reachable due to first check, but safe fallback
            return False

    except Exception:
        return False

    return True