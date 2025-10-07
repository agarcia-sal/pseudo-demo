from typing import List


def string_sequence(quantifier_m: int) -> str:
    result_list: List[str] = []
    counter_k: int = 0
    while counter_k <= quantifier_m:
        temp_val: int = counter_k
        temp_str: str = str(temp_val)
        result_list.append(temp_str)
        counter_k += 1

    separator: str = " "
    final_string: str = ""
    index_r: int = 0

    if len(result_list) == 0:
        final_string = ""
    else:
        while True:
            final_string += result_list[index_r]
            index_r += 1
            if index_r < len(result_list):
                final_string += separator
            if index_r >= len(result_list):
                break

    return final_string