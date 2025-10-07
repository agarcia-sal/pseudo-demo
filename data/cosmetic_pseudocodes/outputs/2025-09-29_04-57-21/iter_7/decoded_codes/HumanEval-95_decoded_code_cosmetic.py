from typing import Mapping, Any


def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    keys = list(mapping.keys())
    if len(keys) == 0:
        return False

    state_marker: str = "start"
    idx: int = 0
    total_keys: int = len(keys)

    while idx < total_keys:
        current_key = keys[idx]

        if not isinstance(current_key, str):
            state_marker = "mixed"
            break

        if state_marker == "start":
            if current_key == current_key.upper():
                state_marker = "upper"
            elif current_key == current_key.lower():
                state_marker = "lower"
            else:
                break
        elif (state_marker == "upper" and current_key != current_key.upper()) or (
            state_marker == "lower" and current_key != current_key.lower()
        ):
            state_marker = "mixed"
            break
        else:
            break

        idx += 1

    return state_marker == "upper" or state_marker == "lower"