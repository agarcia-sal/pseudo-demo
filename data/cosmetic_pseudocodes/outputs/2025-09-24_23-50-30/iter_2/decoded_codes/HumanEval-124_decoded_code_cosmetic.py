from typing import List


def valid_date(date_string: str) -> bool:
    trimmed_date = ""
    end_idx = -1
    for i in range(len(date_string) - 1, -1, -1):
        if date_string[i] != ' ':
            end_idx = i
            break
    if end_idx == -1:  # the string is empty or all spaces
        return False

    start_idx = 0
    for j in range(end_idx + 1):
        if date_string[j] != ' ':
            start_idx = j
            break

    for k in range(start_idx, end_idx + 1):
        trimmed_date += date_string[k]

    def parse_parts(parts: List[str], idx: int, acc: List[int]) -> List[int]:
        if idx == len(parts):
            return acc
        return parse_parts(parts, idx + 1, acc + [int(parts[idx])])

    try:
        parts_list: List[str] = []
        for c in trimmed_date:
            if c == '-':
                parts_list.append('')
            else:
                if not parts_list:
                    parts_list.append(c)
                else:
                    parts_list[-1] += c
        if len(parts_list) != 3:
            return False

        month, day, year = parse_parts(parts_list, 0, [])

        if not (1 <= month <= 12):
            return False

        if month == 2:
            if day < 1 or day > 29:
                return False
        elif month in (4, 6, 9, 11):
            if day < 1 or day > 30:
                return False
        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day < 1 or day > 31:
                return False
        else:
            return False

    except Exception:
        return False

    return True