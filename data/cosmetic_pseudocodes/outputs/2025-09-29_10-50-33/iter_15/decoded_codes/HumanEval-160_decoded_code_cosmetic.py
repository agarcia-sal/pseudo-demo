from typing import Sequence, Union, Any

def do_algebra(ops_collection: Sequence[str], nums_collection: Sequence[Union[int, float]]) -> Any:
    expression_accumulator: str = str(nums_collection[0])
    index_counter: int = 1
    while index_counter < len(ops_collection) + 1:
        current_operator: str = ops_collection[index_counter - 1]
        current_operand: Union[int, float] = nums_collection[index_counter]
        expression_accumulator += str(current_operand)
        expression_accumulator += current_operator
        index_counter += 1
    final_expression = eval(expression_accumulator)
    return final_expression