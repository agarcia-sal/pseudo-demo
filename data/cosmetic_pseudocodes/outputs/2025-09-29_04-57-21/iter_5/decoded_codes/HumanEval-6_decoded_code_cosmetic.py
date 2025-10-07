from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        nesting_counter = 0
        peak_nesting = 0

        index = 0
        while index < len(group_string):
            symbol = group_string[index]
            if symbol == '(':
                nesting_counter += 1
                if peak_nesting < nesting_counter:
                    peak_nesting = nesting_counter
            else:
                nesting_counter -= 1
            index += 1

        return peak_nesting

    segments: List[str] = []
    start_pos = 0
    end_pos = 0
    length = len(parentheses_string)
    while end_pos <= length:
        if end_pos == length or parentheses_string[end_pos] == ' ':
            part = parentheses_string[start_pos:end_pos]
            if part != '':
                segments.append(part)
            start_pos = end_pos + 1
        end_pos += 1

    results: List[int] = []
    iterator = 0
    while iterator < len(segments):
        results.append(parse_paren_group(segments[iterator]))
        iterator += 1

    return results