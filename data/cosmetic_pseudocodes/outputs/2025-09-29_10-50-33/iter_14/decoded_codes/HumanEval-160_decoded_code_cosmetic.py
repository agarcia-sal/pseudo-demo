from typing import List, Union

def do_algebra(input_operators: List[str], input_operands: List[Union[int, float]]) -> Union[int, float]:
    def build_expression(index: int, constructed_str: str) -> Union[int, float]:
        if index >= len(input_operands):
            return eval(constructed_str)  # Evaluate built expression string
        next_token = f"{input_operators[index]}{input_operands[index]}"
        return build_expression(index + 1, constructed_str + next_token)
    return build_expression(1, str(input_operands[0]))