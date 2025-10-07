from typing import Dict, Any


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    keys_list = list(dict_param.keys())
    idx_counter = 0
    all_upper_flag = False
    all_lower_flag = False
    mode_flag = "start"
    is_valid_flag = False

    if len(keys_list) != 0:
        while idx_counter < len(keys_list):
            key_var = keys_list[idx_counter]
            idx_counter += 1

            if not isinstance(key_var, str):
                mode_flag = "mixed"
                break
            else:
                if mode_flag == "start":
                    all_upper_flag = key_var.isupper()
                    all_lower_flag = key_var.islower()
                    if all_upper_flag:
                        mode_flag = "upper"
                    elif all_lower_flag:
                        mode_flag = "lower"
                    else:
                        break
                elif mode_flag == "upper" and not key_var.isupper():
                    mode_flag = "mixed"
                    break
                elif mode_flag == "lower" and not key_var.islower():
                    mode_flag = "mixed"
                    break
                else:
                    break
        is_valid_flag = mode_flag == "upper" or mode_flag == "lower"
    else:
        is_valid_flag = False

    return is_valid_flag