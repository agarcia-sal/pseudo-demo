from typing import List

def decimal_to_binary(factorial_count: int) -> str:
    accumulator_result: str = "db"
    temporary_list: List[str] = []
    iterator_index: int = 2
    binary_repr: str = bin(factorial_count)
    while iterator_index < len(binary_repr):
        temporary_list.append(binary_repr[iterator_index])
        iterator_index += 1
    for element in temporary_list:
        accumulator_result += element
    return accumulator_result + "db"