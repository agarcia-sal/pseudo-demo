from typing import Any, Dict


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    key_count: int = len(dict_param.keys())
    if not (key_count > 0):
        return False

    current_status: str = "start"
    keys = list(dict_param.keys())

    for index_var in range(key_count):
        current_key = keys[index_var]

        if not isinstance(current_key, str):
            current_status = "mixed"
            break

        if current_status == "start":
            if current_key.isupper():
                current_status = "upper"
            else:
                if current_key.islower():
                    current_status = "lower"
                else:
                    break

        elif current_status == "upper":
            if not current_key.isupper():
                current_status = "mixed"
                break

        elif current_status == "lower":
            if not current_key.islower():
                current_status = "mixed"
                break

    result_flag: bool = (current_status == "upper") or (current_status == "lower")
    return result_flag