from typing import List

def parse_nested_parens(input_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        def helper(current_index: int, depth_acc: int, max_acc: int) -> int:
            if current_index >= len(substring):
                return max_acc
            ch = substring[current_index]
            new_depth = depth_acc + 1 if ch == '(' else depth_acc - 1
            new_max = new_depth if new_depth > max_acc else max_acc
            return helper(current_index + 1, new_depth, new_max)
        return helper(0, 0, 0)

    parts: List[str] = []
    start_idx = 0
    i = 0
    length = len(input_string)
    while i < length:
        if input_string[i] == ' ':
            if i - start_idx > 0:
                parts.append(input_string[start_idx:i])
            start_idx = i + 1
        i += 1
    if length - start_idx > 0:
        parts.append(input_string[start_idx:length])

    result: List[int] = []
    for segment in parts:
        if len(segment) > 0:
            result.append(parse_paren_group(segment))
    return result