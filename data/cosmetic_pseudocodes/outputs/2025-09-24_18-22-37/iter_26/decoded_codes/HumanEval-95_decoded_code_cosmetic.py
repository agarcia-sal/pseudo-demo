from typing import Any


def check_dict_case(dict_obj: dict[Any, Any]) -> bool:
    key_list = list(dict_obj.keys())
    idx = len(key_list) - 1
    if idx < 0:
        return False

    status_flag = "start"
    while idx >= 0:
        temp_key = key_list[idx]
        idx -= 1

        if not isinstance(temp_key, str):
            status_flag = "mixed"
            break

        if status_flag == "start":
            cond1 = (temp_key == temp_key.upper())
            cond2 = (temp_key == temp_key.lower())
            if cond1:
                status_flag = "upper"
            else:
                if cond2:
                    status_flag = "lower"
                else:
                    break
        else:
            if status_flag == "upper" and temp_key != temp_key.upper():
                status_flag = "mixed"
                break
            else:
                if status_flag == "lower" and temp_key != temp_key.lower():
                    status_flag = "mixed"
                    break
                else:
                    break

    flag_string_status = status_flag == "upper" or status_flag == "lower"
    return flag_string_status