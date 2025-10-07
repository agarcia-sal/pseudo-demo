from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        nesting_level = 0
        peak_level = 0

        def iterate(idx: int) -> int:
            nonlocal nesting_level, peak_level
            if idx >= len(group_string):
                return peak_level
            symbol = group_string[idx]
            if symbol == '(':
                nesting_level += 1
                if peak_level < nesting_level:
                    peak_level = nesting_level
            else:
                nesting_level -= 1
            return iterate(idx + 1)

        return iterate(0)

    tokens = [x for x in parentheses_string.split(' ') if x != '']
    result_list: List[int] = []

    def process_group(i: int) -> List[int]:
        if i >= len(tokens):
            return result_list
        result_list.append(parse_paren_group(tokens[i]))
        return process_group(i + 1)

    return process_group(0)