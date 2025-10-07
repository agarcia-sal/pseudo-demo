from typing import Any, Dict, List


def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    state_var: str = "start"
    keys_list: List[Any] = list(dict_obj.keys())
    if not keys_list:
        return False

    def iterate_keys(index: int) -> None:
        nonlocal state_var
        if index >= len(keys_list):
            return

        current_key = keys_list[index]

        # Emulate switch True with if-elif-else in Python
        if not isinstance(current_key, str):
            state_var = "mixed"
            return
        elif state_var == "start":
            if current_key.isupper():
                state_var = "upper"
                iterate_keys(index + 1)
            elif current_key.islower():
                state_var = "lower"
                iterate_keys(index + 1)
            else:
                return
        elif (state_var == "upper" and not current_key.isupper()) or (
            state_var == "lower" and not current_key.islower()
        ):
            state_var = "mixed"
            return
        else:
            return

    iterate_keys(0)
    return state_var == "upper" or state_var == "lower"