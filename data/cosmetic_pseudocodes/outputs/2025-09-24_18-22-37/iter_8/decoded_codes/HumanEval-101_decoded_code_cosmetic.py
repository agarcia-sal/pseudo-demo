from typing import List

def words_string(str_param: str) -> List[str]:
    if not str_param:
        return []

    char_accumulator_var: List[str] = []
    idx_var: int = 0

    while idx_var < len(str_param):
        current_char_var: str = str_param[idx_var]
        if current_char_var == ',':
            char_accumulator_var.append(' ')
        else:
            char_accumulator_var.append(current_char_var)
        idx_var += 1

    tmp_str_var: str = ''
    idx_var = 0
    while idx_var < len(char_accumulator_var):
        tmp_str_var += char_accumulator_var[idx_var]
        idx_var += 1

    return tmp_str_var.split()