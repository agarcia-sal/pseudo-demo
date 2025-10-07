from typing import List


def string_sequence(integer_n: int) -> str:
    result_array: List[str] = ["" for _ in range(integer_n + 1)]
    index_var: int = 0

    while index_var <= integer_n:
        result_array[index_var] = str(index_var)
        index_var += 1

    combined_string: str = ""

    if len(result_array) == 0:
        return combined_string

    combined_string = result_array[0]
    position: int = 1

    while position < len(result_array):
        combined_string += " " + result_array[position]
        position += 1

    return combined_string