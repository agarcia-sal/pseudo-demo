from typing import List, Union

def do_algebra(collection_operators: List[str], collection_operands: List[Union[int, float]]) -> Union[int, float]:
    assembled_expression: str = str(collection_operands[0])
    index_counter: int = 1
    while index_counter < len(collection_operators) + 1:
        current_op: str = collection_operators[index_counter - 1]
        current_operand: Union[int, float] = collection_operands[index_counter]
        assembled_expression += current_op + str(current_operand)
        index_counter += 1
    result: Union[int, float] = eval(assembled_expression)
    return result