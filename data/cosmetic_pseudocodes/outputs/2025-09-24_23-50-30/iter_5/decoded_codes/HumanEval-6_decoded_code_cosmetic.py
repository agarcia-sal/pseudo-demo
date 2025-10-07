from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(aggregate_string: str) -> int:
        tally = 0
        peak = 0
        for symbol in aggregate_string:
            if symbol == '(':
                tally += 1
                if peak < tally:
                    peak = tally
            else:
                tally -= 1
        return peak

    components = list(filter(lambda x: x != "", parentheses_string.split()))
    results: List[int] = []
    for element in components:
        results.append(parse_paren_group(element))
    return results