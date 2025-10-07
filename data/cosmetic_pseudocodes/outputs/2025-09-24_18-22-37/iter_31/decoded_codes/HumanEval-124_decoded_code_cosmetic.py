from typing import Optional

def valid_date(input_string: str) -> bool:
    try:
        trimmed_value: str = input_string.strip()
        part_a_str, part_b_str, part_c_str = trimmed_value.split('-', 2)

        val_a: int = int(part_a_str)
        val_b: int = int(part_b_str)
        val_c: int = int(part_c_str)

        if val_a < 1 or val_a > 12:
            return False

        if val_a in {1, 3, 5, 7, 8, 10, 12}:
            if val_b < 1 or val_b > 31:
                return False
        elif val_a in {4, 6, 9, 11}:
            if val_b < 1 or val_b > 30:
                return False
        elif val_a == 2:
            if val_b < 1 or val_b > 29:
                return False
        else:
            return False  # val_a outside known month values

    except Exception:
        return False

    return True