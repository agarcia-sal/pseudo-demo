from typing import Any, Dict, List


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def analyze_keys(keys_list: List[Any], idx: int, current_state: str) -> bool:
        if idx >= len(keys_list):
            return current_state == "upper" or current_state == "lower"

        element = keys_list[idx]
        if not isinstance(element, str):
            return False

        if current_state == "start":
            if element == element.upper():
                return analyze_keys(keys_list, idx + 1, "upper")
            elif element == element.lower():
                return analyze_keys(keys_list, idx + 1, "lower")
            else:
                return False
        elif current_state == "upper":
            if element != element.upper():
                return False
            return analyze_keys(keys_list, idx + 1, current_state)
        elif current_state == "lower":
            if element != element.lower():
                return False
            return analyze_keys(keys_list, idx + 1, current_state)
        else:
            return False

    keys_collection = list(dictionary.keys())
    if not keys_collection:
        return False
    return analyze_keys(keys_collection, 0, "start")