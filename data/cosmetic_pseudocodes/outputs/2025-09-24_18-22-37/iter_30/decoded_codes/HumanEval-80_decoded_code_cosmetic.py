from typing import Sequence, Union

def is_happy(algo_var: Union[str, Sequence[str]]) -> bool:
    if len(algo_var) < 3:
        return False

    pos = 0
    while pos <= len(algo_var) - 3:
        first_char = algo_var[pos]
        second_char = algo_var[pos + 1]
        third_char = algo_var[pos + 2]

        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False

        pos += 1

    return True