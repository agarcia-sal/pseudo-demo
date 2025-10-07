from typing import Sequence


def is_happy(param1: Sequence[str]) -> bool:
    counter_var: int = 0
    len_var: int = len(param1)
    if len_var < 3:
        return False
    while counter_var <= len_var - 3:
        # If not all three characters at current window are distinct, return False
        if not (
            param1[counter_var] != param1[counter_var + 1]
            and param1[counter_var + 1] != param1[counter_var + 2]
            and param1[counter_var] != param1[counter_var + 2]
        ):
            return False
        counter_var += 1
    return True