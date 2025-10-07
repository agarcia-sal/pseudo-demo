from typing import Any


def check_dict_case(dict_obj: dict[Any, Any]) -> bool:
    tuples_seq = list(dict_obj.keys())

    if len(tuples_seq) == 0:
        return False

    state_flag = "start"

    def iterate_keys(position: int) -> None:
        nonlocal state_flag

        if position == len(tuples_seq):
            return

        current_k = tuples_seq[position]

        if not isinstance(current_k, str):
            state_flag = "mixed"
            return

        if state_flag == "start":
            if current_k == current_k.upper():
                state_flag = "upper"
            elif current_k == current_k.lower():
                state_flag = "lower"
            else:
                return
        elif (state_flag == "upper" and current_k != current_k.upper()) or (
            state_flag == "lower" and current_k != current_k.lower()
        ):
            state_flag = "mixed"
            return
        else:
            return

        iterate_keys(position + 1)

    iterate_keys(0)

    return state_flag == "upper" or state_flag == "lower"