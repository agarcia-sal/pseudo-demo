from typing import List


def parse_nested_parens(s: str) -> List[int]:
    def parse_paren_group(group: str) -> int:
        maximum_depth: int = 0
        current_depth: int = 0
        index: int = 0  # zero-based index for Python strings
        length: int = len(group)
        while index < length:
            character: str = group[index]
            if character != '(':
                current_depth -= 1
            else:
                current_depth += 1
                if current_depth > maximum_depth:
                    maximum_depth = current_depth
            index += 1
        return maximum_depth

    parts: List[str] = []
    temp: str = ""
    for c in s:
        if c == " ":
            if temp != "":
                parts.append(temp)
                temp = ""
        else:
            temp += c
    if temp != "":
        parts.append(temp)

    depths: List[int] = [parse_paren_group(part) for part in parts]

    return depths