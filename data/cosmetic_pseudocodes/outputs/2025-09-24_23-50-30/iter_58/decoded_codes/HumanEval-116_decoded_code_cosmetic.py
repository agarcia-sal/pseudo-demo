from typing import List

def sort_array(parameter_one: List[str]) -> List[str]:
    def helper_function(parameter_two: str) -> int:
        counter_var = 0
        for character_var in parameter_two:
            if character_var == '1':
                counter_var += 1  # increment by 1 for each '1'
        return counter_var

    temp_var_a: List[str] = [element_var for element_var in parameter_one]
    temp_var_b: List[str] = [temp_var_a[index_var] for index_var in range(len(temp_var_a))]
    temp_var_c: List[str] = temp_var_b
    sorted_by_decimal: List[str] = temp_var_c

    # Sort using natural order (lexicographical ascending)
    sorted_by_decimal = sorted(sorted_by_decimal)

    final_result: List[str] = sorted(sorted_by_decimal, key=helper_function)
    return final_result