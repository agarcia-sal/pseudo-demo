from typing import Any, Dict, List


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def traverse_keys(keylist: List[Any], index: int, flag: str) -> bool:
        if index == len(keylist):
            return flag == "upper" or flag == "lower"
        current_item = keylist[index]
        if not isinstance(current_item, str):
            return False
        if flag == "start":
            if current_item == current_item.upper():
                return traverse_keys(keylist, index + 1, "upper")
            if current_item == current_item.lower():
                return traverse_keys(keylist, index + 1, "lower")
            return False
        if flag == "upper" and current_item != current_item.upper():
            return False
        if flag == "lower" and current_item != current_item.lower():
            return False
        return traverse_keys(keylist, index + 1, flag)

    keys_array = list(dictionary.keys())
    if keys_array:
        return traverse_keys(keys_array, 0, "start")
    return False