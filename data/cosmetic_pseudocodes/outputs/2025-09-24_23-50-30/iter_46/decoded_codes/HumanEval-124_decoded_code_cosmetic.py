from typing import Union


def valid_date(input_string: str) -> bool:
    def check_month_day(mm: int, dd: int) -> bool:
        if mm in {1, 3, 5, 7, 8, 10, 12}:
            return 1 <= dd <= 31
        if mm in {4, 6, 9, 11}:
            return 1 <= dd <= 30
        if mm == 2:
            return 1 <= dd <= 29
        return False

    def parse_and_validate(trimmed: str) -> bool:
        try:
            parts_array = trimmed.split('-')
            if len(parts_array) != 3:
                return False
            a = int(parts_array[0])
            b = int(parts_array[1])
            c = int(parts_array[2])
            if a < 1 or a > 12:
                return False
            if not check_month_day(a, b):
                return False
            return True
        except Exception:
            return False

    trimmed_string = input_string.strip()
    return parse_and_validate(trimmed_string)