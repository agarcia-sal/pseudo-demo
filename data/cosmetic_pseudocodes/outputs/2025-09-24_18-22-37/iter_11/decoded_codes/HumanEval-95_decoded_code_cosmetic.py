from typing import Any


def check_dict_case(dict_param: dict[Any, Any]) -> bool:
    flag_state: str = "start"
    keys_list = list(dict_param.keys())
    key_collection_length: int = len(keys_list)

    if key_collection_length <= 0:
        return False

    index_cursor: int = 0
    while index_cursor < key_collection_length:
        key_iter = keys_list[index_cursor]
        key_type_check: bool = isinstance(key_iter, str)

        if not key_type_check:
            flag_state = "mixed"
            break

        if flag_state == "start":
            all_upper_check: bool = key_iter.upper() == key_iter
            all_lower_check: bool = key_iter.lower() == key_iter

            if all_upper_check:
                flag_state = "upper"
            elif all_lower_check:
                flag_state = "lower"
            else:
                break
        else:
            is_state_upper: bool = flag_state == "upper"
            is_state_lower: bool = flag_state == "lower"
            cond_upper_mismatch: bool = is_state_upper and (key_iter.upper() != key_iter)
            cond_lower_mismatch: bool = is_state_lower and (key_iter.lower() != key_iter)

            if cond_upper_mismatch or cond_lower_mismatch:
                flag_state = "mixed"
                break
            else:
                break

        index_cursor += 1

    if flag_state == "upper" or flag_state == "lower":
        return True
    else:
        return False