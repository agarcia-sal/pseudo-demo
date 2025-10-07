from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    index_counter: int = 0
    while index_counter <= integer_n:
        temp_str: str = str(index_counter)
        result_list.append(temp_str)
        index_counter += 1
    output_string: str = " ".join(result_list)
    return output_string