from typing import List


def match_parens(array_param: List[str]) -> str:
    def check_inner(param_string: str) -> bool:
        counter_var = 0
        iterator_var = 0
        while iterator_var < len(param_string):
            current_symbol = param_string[iterator_var]
            if current_symbol == '(':
                counter_var += 1
            else:
                counter_var -= 1
            if counter_var < 0:
                return False
            iterator_var += 1
        return counter_var == 0

    first_concat = array_param[0] + array_param[1]
    second_concat = array_param[1] + array_param[0]
    if check_inner(first_concat) or check_inner(second_concat):
        return 'Yes'
    else:
        return 'No'