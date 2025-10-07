from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(sequence: str) -> int:
        accumulator_a: int = 0
        accumulator_b: int = 0
        for symbol in sequence:
            if symbol == '(':
                accumulator_a += 1
                if accumulator_b < accumulator_a:
                    accumulator_b = accumulator_a
            else:
                accumulator_a -= 1
        return accumulator_b

    split_groups = [item for item in parentheses_string.split(' ') if item]
    result_list: List[int] = [parse_paren_group(element) for element in split_groups]
    return result_list