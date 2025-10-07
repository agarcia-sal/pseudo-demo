from typing import List


def parse_nested_parens(input_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        depth_counter = 0
        max_depth_value = 0
        for symbol in substring:
            if symbol == '(':
                depth_counter += 1
                if max_depth_value < depth_counter:
                    max_depth_value = depth_counter
            else:
                depth_counter -= 1
        return max_depth_value

    token_list: List[str] = []
    buffer = ""
    for ch in input_string:
        if ch == " ":
            token_list.append(buffer)
            buffer = ""
        else:
            buffer += ch
    if buffer != "":
        token_list.append(buffer)

    results: List[int] = []
    i = 0
    while i < len(token_list):
        element = token_list[i]
        if element != "":
            depth_result = parse_paren_group(element)
            results.append(depth_result)
        i += 1

    return results