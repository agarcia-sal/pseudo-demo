from typing import Any


def valid_date(input_str: str) -> bool:
    try:
        trimmed_str: str = input_str.lstrip().rstrip()
        parts: list[str] = trimmed_str.split("-")

        part1: str = parts[0]
        part2: str = parts[1]
        part3: str = parts[2]

        val_a: int = int(part1)
        val_b: int = int(part2)
        val_c: int = int(part3)

        if not (1 <= val_a <= 12):
            return False

        thirtyone_months: list[int] = [1, 3, 5, 7, 8, 10, 12]
        thirty_months: list[int] = [4, 6, 9, 11]

        condition_one: bool = False
        condition_two: bool = False
        condition_three: bool = False

        temp_day_check: bool = val_b < 1

        for num in thirtyone_months:
            if val_a == num:
                condition_one = temp_day_check or val_b > 31

        for num in thirty_months:
            if val_a == num:
                condition_two = temp_day_check or val_b > 30

        if val_a == 2:
            condition_three = temp_day_check or val_b > 29  # 32-3=29 days max in Feb

        if condition_one or condition_two or condition_three:
            return False

    except Exception:
        return False

    return True