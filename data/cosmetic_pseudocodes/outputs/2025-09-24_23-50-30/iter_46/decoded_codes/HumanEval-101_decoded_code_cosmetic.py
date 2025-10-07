from typing import List

def words_string(parameter_one: str) -> List[str]:
    def helper_function(index_accumulator: int, accumulator_list: List[str]) -> List[str]:
        if index_accumulator >= len(parameter_one):
            return accumulator_list
        current_symbol = parameter_one[index_accumulator]
        new_symbol = current_symbol if current_symbol != ',' else ' '
        return helper_function(index_accumulator + 1, accumulator_list + [new_symbol])

    if not len(parameter_one) > 0:
        return []

    preliminary_list = helper_function(0, [])
    merged_string = ''.join(preliminary_list)

    return merged_string.split(' ')