from typing import Any, Dict, List, Literal


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def scan_keys(keys_list: List[Any], position: int, mode: Literal["start", "upper", "lower"]) -> bool:
        if position >= len(keys_list):
            return mode == "upper" or mode == "lower"

        current_key = keys_list[position]
        if not isinstance(current_key, str):
            return False

        if mode == "start":
            if current_key == current_key.upper():
                return scan_keys(keys_list, position + 1, "upper")
            elif current_key == current_key.lower():
                return scan_keys(keys_list, position + 1, "lower")
            else:
                return False
        elif mode == "upper":
            if current_key == current_key.upper():
                return scan_keys(keys_list, position + 1, "upper")
            else:
                return False
        elif mode == "lower":
            if current_key == current_key.lower():
                return scan_keys(keys_list, position + 1, "lower")
            else:
                return False
        else:
            return False

    keys_array = list(dictionary.keys())
    if len(keys_array) == 0:
        return False
    return scan_keys(keys_array, 0, "start")