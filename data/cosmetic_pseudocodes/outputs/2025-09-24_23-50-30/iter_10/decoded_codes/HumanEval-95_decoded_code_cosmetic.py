from typing import Any, Dict, List


def check_dict_case(input_map: Dict[Any, Any]) -> bool:
    keys_set = set(input_map.keys())
    if len(keys_set) == 0:
        return False

    def traverse(keys_list: List[Any], idx: int, mode: str) -> bool:
        if idx >= len(keys_list):
            return mode == "upper" or mode == "lower"

        curr_key = keys_list[idx]
        if not isinstance(curr_key, str):
            return False

        if mode == "start":
            if curr_key.isupper():
                return traverse(keys_list, idx + 1, "upper")
            if curr_key.islower():
                return traverse(keys_list, idx + 1, "lower")
            return False
        if mode == "upper":
            return curr_key.isupper() and traverse(keys_list, idx + 1, "upper")
        if mode == "lower":
            return curr_key.islower() and traverse(keys_list, idx + 1, "lower")
        return False

    return traverse(list(input_map.keys()), 0, "start")