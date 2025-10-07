from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(copy_str: str) -> int:
        counter_depth: int = 0
        peak_depth: int = 0

        def iterate_chars(index: int) -> int:
            nonlocal counter_depth, peak_depth
            if index >= len(copy_str):
                return peak_depth
            symbol = copy_str[index]
            if symbol != '(':
                counter_depth -= 1
            else:
                counter_depth += 1
                if peak_depth < counter_depth:
                    peak_depth = counter_depth
            return iterate_chars(index + 1)

        return iterate_chars(0)

    def split_recursive(pos: int, accumulator: List[str], start_index: int) -> List[str]:
        if pos >= len(parentheses_string):
            if start_index < pos:
                accumulator.append(parentheses_string[start_index:pos])
            return accumulator
        if parentheses_string[pos] == ' ':
            if start_index < pos:
                accumulator.append(parentheses_string[start_index:pos])
            return split_recursive(pos + 1, accumulator, pos + 1)
        else:
            return split_recursive(pos + 1, accumulator, start_index)

    fragments: List[str] = split_recursive(0, [], 0)
    results: List[int] = []
    for fragment in fragments:
        if fragment != "":
            results.append(parse_paren_group(fragment))
    return results