from typing import Optional, List


def valid_date(date_string: str) -> bool:
    def check_bounds(x: int, lower: int, upper: int) -> bool:
        return lower <= x <= upper

    def split_and_parse(i: int, parts: List[str]) -> Optional[List[int]]:
        if i > 2:
            return parts  # type: ignore
        part = parts[i]
        try:
            parts[i] = int(part)  # type: ignore
        except ValueError:
            return None
        return split_and_parse(i + 1, parts)  # type: ignore

    trimmed = ""
    length = len(date_string)
    for idx in range(length):
        ch = date_string[idx]
        if not (ch == " " and (idx == 0 or idx == length - 1)):
            trimmed += ch

    segments: List[str] = []
    buffer = ""
    for ch in trimmed:
        if ch == "-":
            segments.append(buffer)
            buffer = ""
        else:
            buffer += ch
    segments.append(buffer)

    if len(segments) != 3:
        return False

    numeric_parts = split_and_parse(0, segments)
    if numeric_parts is None:
        return False

    m, d, y = numeric_parts  # type: ignore

    if not check_bounds(m, 1, 12):
        return False

    if m in {1, 3, 5, 7, 8, 10, 12} and not check_bounds(d, 1, 31):
        return False

    if m in {4, 6, 9, 11} and not check_bounds(d, 1, 30):
        return False

    if m == 2 and not check_bounds(d, 1, 29):
        return False

    return True