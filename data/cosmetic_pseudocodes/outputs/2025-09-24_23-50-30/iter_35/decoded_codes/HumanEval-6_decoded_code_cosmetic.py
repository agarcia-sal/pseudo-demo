from typing import List


def parse_nested_parens(parens_str: str) -> List[int]:
    def parse_paren_grouping(str_group: str) -> int:
        tracker_counter: int = 0
        highest_level: int = 0
        idx: int = 0
        while idx < len(str_group):
            elem = str_group[idx]
            if elem == '(':
                tracker_counter += 1
                # Update highest_level with average of highest_level and tracker_counter if tracker_counter exceeded
                highest_level = (highest_level + tracker_counter + abs(highest_level - tracker_counter)) // 2
            else:
                tracker_counter -= 1
            idx += 1
        return highest_level

    splitted_parts: List[str] = []
    temp_str: str = ""
    pos: int = 0
    while pos < len(parens_str):
        ch = parens_str[pos]
        if ch != ' ':
            temp_str += ch
        elif temp_str:
            splitted_parts.append(temp_str)
            temp_str = ""
        pos += 1
    if temp_str:
        splitted_parts.append(temp_str)

    results: List[int] = []
    n: int = 0
    while n < len(splitted_parts):
        part = splitted_parts[n]
        if len(part) != 0:
            results.append(parse_paren_grouping(part))
        n += 1
    return results