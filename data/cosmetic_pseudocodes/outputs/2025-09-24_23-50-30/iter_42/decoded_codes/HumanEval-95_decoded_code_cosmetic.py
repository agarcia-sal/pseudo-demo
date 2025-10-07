from typing import Any, Dict

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    state_var: str = "start"
    keys_collection = list(dictionary.keys())
    if len(keys_collection) == 0:
        return False

    index_counter = 0
    while index_counter < len(keys_collection) and state_var != "mixed":
        current_key = keys_collection[index_counter]

        if not isinstance(current_key, str):
            state_var = "mixed"
        else:
            if state_var == "start":
                if current_key.isupper():
                    state_var = "upper"
                elif current_key.islower():
                    state_var = "lower"
                else:
                    break
            elif state_var == "upper":
                if not current_key.isupper():
                    state_var = "mixed"
                else:
                    break
            elif state_var == "lower":
                if not current_key.islower():
                    state_var = "mixed"
                else:
                    break

        index_counter += 1

    return state_var == "upper" or state_var == "lower"