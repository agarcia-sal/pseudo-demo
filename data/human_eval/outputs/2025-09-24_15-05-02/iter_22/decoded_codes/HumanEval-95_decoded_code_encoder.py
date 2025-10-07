from typing import Any, Dict

def check_dict_case(input_dictionary: Dict[Any, Any]) -> bool:
    if len(input_dictionary) == 0:
        return False
    case_state = "start"
    for key in input_dictionary.keys():
        if not isinstance(key, str):
            case_state = "mixed"
            break
        if case_state == "start":
            if key.isupper():
                case_state = "upper"
            elif key.islower():
                case_state = "lower"
            else:
                break
        elif (case_state == "upper" and not key.isupper()) or (case_state == "lower" and not key.islower()):
            case_state = "mixed"
            break
        else:
            break
    return case_state == "upper" or case_state == "lower"