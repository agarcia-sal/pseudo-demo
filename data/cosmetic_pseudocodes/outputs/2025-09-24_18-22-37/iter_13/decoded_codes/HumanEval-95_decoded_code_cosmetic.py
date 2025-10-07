from typing import Mapping, Any


def check_dict_case(container: Mapping[Any, Any]) -> bool:
    keys = list(container.keys())
    if len(keys) == 0:
        return False

    state_marker = "start"
    max_index = len(keys)
    iterator_index = 0

    while iterator_index < max_index:
        current_key = keys[iterator_index]

        if not isinstance(current_key, str):
            state_marker = "mixed"
            break

        if state_marker == "start":
            temp_is_upper = current_key.isupper()
            temp_is_lower = current_key.islower()

            if temp_is_upper:
                state_marker = "upper"
            elif temp_is_lower:
                state_marker = "lower"
            else:
                break

        elif state_marker == "upper":
            if not current_key.isupper():
                state_marker = "mixed"
            break  # exit loop after processing this key

        elif state_marker == "lower":
            if not current_key.islower():
                state_marker = "mixed"
            break  # exit loop after processing this key

        else:
            break  # any other state, exit loop

        iterator_index += 1

    return state_marker in ("upper", "lower")