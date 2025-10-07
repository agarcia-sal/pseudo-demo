from typing import Dict, Any


def check_dict_case(dict_arg: Dict[Any, Any]) -> bool:
    if len(dict_arg) == 0:
        return False

    var_state: str = "start"
    for loop_var in dict_arg.keys():
        if not isinstance(loop_var, str):
            var_state = "mixed"
            break
        if var_state == "start":
            if loop_var == loop_var.upper():
                var_state = "upper"
            elif loop_var == loop_var.lower():
                var_state = "lower"
            else:
                break
        else:
            if var_state == "upper" and loop_var != loop_var.upper():
                var_state = "mixed"
                break
            elif var_state == "lower" and loop_var != loop_var.lower():
                var_state = "mixed"
                break
            else:
                break

    return var_state == "upper" or var_state == "lower"