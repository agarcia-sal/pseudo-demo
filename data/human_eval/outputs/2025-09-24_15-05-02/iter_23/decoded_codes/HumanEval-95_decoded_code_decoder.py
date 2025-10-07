from typing import Dict, Any

def check_dict_case(input_dict: Dict[Any, Any]) -> bool:
    if len(input_dict.keys()) == 0:
        return False
    else:
        state: str = "start"
        for key in input_dict.keys():
            if not isinstance(key, str):
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
            else:
                break
        return state == "upper" or state == "lower"