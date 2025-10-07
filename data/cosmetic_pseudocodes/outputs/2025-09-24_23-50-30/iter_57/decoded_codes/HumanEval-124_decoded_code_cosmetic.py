from typing import List


def valid_date(input_string: str) -> bool:
    def is_invalid_month(numeral: int) -> bool:
        return not (1 <= numeral <= 12)

    def is_invalid_day(month_val: int, day_val: int) -> bool:
        if month_val == 2:
            return day_val < 1 or day_val > 29
        elif month_val in {4, 6, 9, 11}:
            return day_val < 1 or day_val > 30
        elif month_val in {1, 3, 5, 7, 8, 10, 12}:
            return day_val < 1 or day_val > 31
        else:
            return True

    trimmed_str: str = input_string.strip()

    # parse_parts function is declared but unused, retaining structure
    def parse_parts(lst: List[str], idx: int) -> bool:
        if idx == 3:
            return True
        if idx == 0:
            return True

    try:
        parts: List[str] = []
        pos: int = 0
        start: int = 0
        length_trimmed: int = len(trimmed_str)

        while pos <= length_trimmed:
            if pos == length_trimmed or trimmed_str[pos] == '-':
                # substring from start to pos-1 inclusive; if start > pos-1, empty string
                parts.append(trimmed_str[start:pos])
                start = pos + 1
            pos += 1

        if len(parts) != 3:
            return False

        m = int(parts[0])
        d = int(parts[1])
        y = int(parts[2])

        if is_invalid_month(m) or is_invalid_day(m, d):
            return False

    except (ValueError, IndexError):
        return False

    return True