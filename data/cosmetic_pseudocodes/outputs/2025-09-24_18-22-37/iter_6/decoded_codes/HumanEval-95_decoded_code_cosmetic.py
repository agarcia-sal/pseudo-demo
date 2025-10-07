from typing import Mapping, Any


def check_dict_case(map: Mapping[Any, Any]) -> bool:
    count = len(map)
    if count == 0:
        return False

    state = "start"
    keys_collection = list(map.keys())
    idx = 0

    while idx < count:
        current_key = keys_collection[idx]

        if not isinstance(current_key, str):
            state = "mixed"
            break

        if state == "start":
            if current_key.upper() == current_key:
                state = "upper"
            elif current_key.lower() == current_key:
                state = "lower"
            else:
                break

        else:
            if (state == "upper" and current_key.upper() != current_key) or (
                state == "lower" and current_key.lower() != current_key
            ):
                state = "mixed"
                break
            else:
                break
        idx += 1

    return state == "upper" or state == "lower"