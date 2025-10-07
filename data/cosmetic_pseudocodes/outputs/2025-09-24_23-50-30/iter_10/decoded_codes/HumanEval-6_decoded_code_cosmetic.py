from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(string_chunk: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0
        index: int = 0

        while index < len(string_chunk):
            symbol: str = string_chunk[index]
            index += 1

            if symbol == '(':
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
                continue
            # for any other symbol (only ')' expected), decrease depth
            depth_counter -= 1

        return peak_depth

    segments: List[str] = []
    start: int = 0

    for position in range(len(parentheses_string) + 1):
        if position == len(parentheses_string) or parentheses_string[position] == ' ':
            if start < position:
                segments.append(parentheses_string[start:position])
            start = position + 1

    results: List[int] = []
    iterator: int = 0

    while iterator < len(segments):
        results.append(parse_paren_group(segments[iterator]))
        iterator += 1

    return results