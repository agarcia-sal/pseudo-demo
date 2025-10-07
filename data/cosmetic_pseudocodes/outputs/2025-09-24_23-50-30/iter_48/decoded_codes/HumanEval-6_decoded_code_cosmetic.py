from typing import List


def parse_nested_parens(string_input: str) -> List[int]:
    def parse_paren_group(string_piece: str) -> int:
        counter_depth = 0
        highest_depth = 0
        index = 0
        while index < len(string_piece):
            char = string_piece[index]
            if char == '(':
                counter_depth += 1
                if highest_depth < counter_depth:
                    highest_depth = counter_depth
            elif char == ')':
                counter_depth -= 1
            index += 1
        return highest_depth

    parts: List[str] = []
    start = 0
    pos = 0
    length = len(string_input)
    while pos <= length:
        if pos == length or string_input[pos] == ' ':
            if pos - start > 0:
                parts.append(string_input[start:pos])
            start = pos + 1
        pos += 1

    results: List[int] = []
    idx = 0
    while idx < len(parts):
        val = parts[idx]
        if val != '':
            results.append(parse_paren_group(val))
        idx += 1
    return results