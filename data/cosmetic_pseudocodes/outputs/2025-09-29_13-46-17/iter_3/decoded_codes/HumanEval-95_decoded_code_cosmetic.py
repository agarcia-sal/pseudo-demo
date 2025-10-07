from typing import Any, Dict, List


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def analyze_key_list(keys_list: List[Any], current_state: str, index: int) -> str:
        if index >= len(keys_list):
            return current_state

        current_key = keys_list[index]

        if not isinstance(current_key, str):
            return "mixed"

        new_state = current_state

        if current_state == "start":
            if current_key == current_key.upper():
                new_state = "upper"
            elif current_key == current_key.lower():
                new_state = "lower"
            else:
                return "mixed"
        else:
            if (new_state == "upper" and current_key != current_key.upper()) or (
                new_state == "lower" and current_key != current_key.lower()
            ):
                return "mixed"

        return analyze_key_list(keys_list, new_state, index + 1)

    keys_array = list(dictionary.keys())
    if len(keys_array) == 0:
        return False

    final_state = analyze_key_list(keys_array, "start", 0)
    return final_state == "upper" or final_state == "lower"