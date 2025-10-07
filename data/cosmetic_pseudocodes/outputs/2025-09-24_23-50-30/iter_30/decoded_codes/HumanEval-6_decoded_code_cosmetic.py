from typing import List, Callable

def parse_nested_parens(input_sequence: str) -> List[int]:
    def parse_paren_group_a(input_fragment: str) -> int:
        depth_counter = 0
        depth_max = 0
        for ch in input_fragment:
            if ch == '(':
                depth_counter += 1
                if depth_counter > depth_max:
                    depth_max = depth_counter
            else:
                depth_counter -= 1
        return depth_max

    segment_list: List[str] = []
    start_index = 1
    length = len(input_sequence)
    for i in range(1, length + 2):
        if i > length or input_sequence[i - 1] == ' ':
            segment = input_sequence[start_index - 1 : i - 1]
            if len(segment) > 0:
                segment_list.append(segment)
            start_index = i + 1

    def map_function(lst: List[str], f: Callable[[str], int]) -> List[int]:
        result: List[int] = []
        pos = 1
        while pos <= len(lst):
            result.append(f(lst[pos - 1]))
            pos += 1
        return result

    return map_function(segment_list, parse_paren_group_a)