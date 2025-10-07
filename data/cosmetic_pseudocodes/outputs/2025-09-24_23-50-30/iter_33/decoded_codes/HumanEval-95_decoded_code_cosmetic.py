from typing import Dict, Any

def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    if not (0 < len(dict_param.keys())):
        return False
    else:
        mode_state: str = "start"
        for element_key in dict_param.keys():
            if not isinstance(element_key, str):
                mode_state = "mixed"
                break
            if mode_state == "start":
                if element_key == element_key.upper():
                    mode_state = "upper"
                else:
                    if element_key == element_key.lower():
                        mode_state = "lower"
                    else:
                        break
            elif mode_state == "upper":
                if element_key != element_key.upper():
                    mode_state = "mixed"
                break
            elif mode_state == "lower":
                if element_key != element_key.lower():
                    mode_state = "mixed"
                break
            else:
                break
        return mode_state == "upper" or mode_state == "lower"