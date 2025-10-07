from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys_array = list(dictionary.keys())
    if len(keys_array) == 0:
        return False

    current_state: str = "start"
    index_counter: int = 0
    while index_counter < len(keys_array):
        current_key = keys_array[index_counter]

        if not isinstance(current_key, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if current_key == current_key.upper() and current_key != current_key.lower():
                current_state = "upper"
            elif current_key == current_key.lower() and current_key != current_key.upper():
                current_state = "lower"
            else:
                break
        elif (current_state == "upper" and current_key != current_key.upper()) or (
            current_state == "lower" and current_key != current_key.lower()
        ):
            current_state = "mixed"
            break
        else:
            break

        index_counter += 1

    return current_state == "upper" or current_state == "lower"