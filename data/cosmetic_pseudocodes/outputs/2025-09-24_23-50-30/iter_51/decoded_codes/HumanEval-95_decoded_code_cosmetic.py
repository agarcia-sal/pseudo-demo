from typing import Any, Dict, Union

def check_dict_case(dictionary_input: Dict[Any, Any]) -> bool:
    def iterate_keys(index_param: int, state_param: str) -> Union[str, bool]:
        keys = list(dictionary_input.keys())
        if index_param >= len(keys):
            return state_param
        current_key = keys[index_param]
        if not isinstance(current_key, str):
            return "mixed"
        if state_param == "start":
            if current_key == current_key.upper() and current_key != current_key.lower():
                return iterate_keys(index_param + 1, "upper")
            elif current_key == current_key.lower() and current_key != current_key.upper():
                return iterate_keys(index_param + 1, "lower")
            else:
                return "mixed"
        elif state_param == "upper":
            if current_key == current_key.upper() and current_key != current_key.lower():
                return iterate_keys(index_param + 1, "upper")
            else:
                return "mixed"
        elif state_param == "lower":
            if current_key == current_key.lower() and current_key != current_key.upper():
                return iterate_keys(index_param + 1, "lower")
            else:
                return "mixed"
        else:
            return "mixed"

    if len(dictionary_input) == 0:
        return False
    final_state = iterate_keys(0, "start")
    return final_state == "upper" or final_state == "lower"