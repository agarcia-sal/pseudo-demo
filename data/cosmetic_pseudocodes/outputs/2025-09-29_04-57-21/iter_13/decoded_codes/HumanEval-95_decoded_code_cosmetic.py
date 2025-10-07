from typing import Dict, Any, List


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys = list(dictionary.keys())
    if not keys:
        return False

    mode: str = "init"

    def process_keys(keys_list: List[Any], index: int) -> bool:
        nonlocal mode
        if index == len(keys_list):
            return True

        current_key = keys_list[index]
        if not isinstance(current_key, str):
            mode = "mixed"
            return False

        if mode == "init":
            if current_key.isupper():
                mode = "upper"
            elif current_key.islower():
                mode = "lower"
            else:
                return False
        else:
            if (mode == "upper" and not current_key.isupper()) or (mode == "lower" and not current_key.islower()):
                mode = "mixed"
                return False
            if not ((mode == "upper" and current_key.isupper()) or (mode == "lower" and current_key.islower())):
                return False

        return process_keys(keys_list, index + 1)

    return process_keys(keys, 0)