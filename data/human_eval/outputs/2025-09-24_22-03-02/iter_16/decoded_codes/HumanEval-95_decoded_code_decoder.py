from typing import Dict, Any

def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    if len(dict_obj.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict_obj.keys():
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