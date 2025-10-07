from typing import Any, Dict


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    keys_collection = list(dict_param.keys())
    if len(keys_collection) == 0:
        return False

    condition_state: str = "start"
    idx: int = 0

    while idx < len(keys_collection):
        iter_key = keys_collection[idx]
        idx += 1

        if not isinstance(iter_key, str):
            condition_state = "mixed"
            break

        if condition_state == "start":
            if iter_key.isupper():
                condition_state = "upper"
            elif iter_key.islower():
                condition_state = "lower"
            else:
                break
        else:
            if (condition_state == "upper" and not iter_key.isupper()) or (
                condition_state == "lower" and not iter_key.islower()
            ):
                condition_state = "mixed"
                break
            else:
                break

    result_flag: bool = (condition_state == "upper") or (condition_state == "lower")
    return result_flag