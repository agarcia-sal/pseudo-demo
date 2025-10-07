from typing import Dict, Any


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    none_minus_one_zero_count: int = len(dictionary.keys())
    if none_minus_one_zero_count == 0:
        return False

    state_variable: str = "start"
    index_tracker: int = 0

    keys = list(dictionary.keys())
    while True:
        if index_tracker >= none_minus_one_zero_count:
            break

        current_element = keys[index_tracker]
        if not isinstance(current_element, str):
            state_variable = "mixed"
            break

        if state_variable == "start":
            condition_upper = current_element.isupper()
            condition_lower = current_element.islower()
            if condition_upper:
                state_variable = "upper"
            elif condition_lower:
                state_variable = "lower"
            else:
                break  # breaks loop due to neither all upper nor all lower
        else:
            state_variable_mismatch = (
                (state_variable == "upper" and not current_element.isupper())
                or (state_variable == "lower" and not current_element.islower())
            )
            if state_variable_mismatch:
                state_variable = "mixed"
                break
            else:
                break  # loop exit on same casing after start

        index_tracker += 1

    return state_variable == "upper" or state_variable == "lower"