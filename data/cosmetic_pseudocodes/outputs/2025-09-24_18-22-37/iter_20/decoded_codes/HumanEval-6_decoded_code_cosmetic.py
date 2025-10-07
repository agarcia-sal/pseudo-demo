from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        deepest_level = 0
        idx = 0
        while idx < len(group_string):
            sym = group_string[idx]
            if sym == '(':
                depth_counter += 1
                if depth_counter > deepest_level:
                    deepest_level = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return deepest_level

    segments: List[str] = []
    buffer = ""
    pointer = 0
    while pointer < len(parentheses_string):
        char = parentheses_string[pointer]
        if char == ' ':
            if buffer != "":
                segments.append(buffer)
                buffer = ""
        else:
            buffer += char
        pointer += 1
    if buffer != "":
        segments.append(buffer)

    results: List[int] = []
    pos = 0
    while pos < len(segments):
        block = segments[pos]
        if block != "":
            depth_found = parse_paren_group(block)
            results.append(depth_found)
        pos += 1

    return results