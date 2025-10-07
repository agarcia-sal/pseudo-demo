from typing import Sequence, Union, Any

def do_algebra(collection_of_operators: Sequence[str], collection_of_operands: Sequence[Any]) -> Any:
    accumulated_expression: str = str(collection_of_operands[0])
    index_counter: int = 1
    while index_counter < len(collection_of_operands):
        current_operator: str = collection_of_operators[index_counter - 1]
        current_operand: Any = collection_of_operands[index_counter]
        accumulated_expression += current_operator
        accumulated_expression += str(current_operand)
        index_counter += 1
    return eval(accumulated_expression)