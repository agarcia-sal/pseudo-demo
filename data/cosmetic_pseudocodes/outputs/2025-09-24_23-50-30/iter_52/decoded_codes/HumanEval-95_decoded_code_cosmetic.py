from typing import Any, Dict, List, Literal


def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    def iterate_keys(keys_list: List[Any], idx: int, current_state: Literal["start", "upper", "lower"]) -> bool:
        if idx >= len(keys_list):
            return current_state == "upper" or current_state == "lower"

        curr_key = keys_list[idx]

        if not isinstance(curr_key, str):
            return False

        if current_state == "start":
            if curr_key.isupper():
                return iterate_keys(keys_list, idx + 1, "upper")
            elif curr_key.islower():
                return iterate_keys(keys_list, idx + 1, "lower")
            else:
                return False
        if current_state == "upper" and not curr_key.isupper():
            return False
        if current_state == "lower" and not curr_key.islower():
            return False
        return iterate_keys(keys_list, idx + 1, current_state)

    keys_array = list(dict_obj.keys())

    if len(keys_array) == 0:
        return False
    else:
        return iterate_keys(keys_array, 0, "start")