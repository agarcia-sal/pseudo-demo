from typing import Any, Dict


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    if not dict_param:
        return False

    status: str = "start"
    key_iter = iter(dict_param.keys())

    while True:
        current_key = next(key_iter, None)
        if current_key is None:
            break

        if not isinstance(current_key, str):
            status = "mixed"
            break

        if status == "start":
            if current_key == current_key.upper():
                status = "upper"
            elif current_key == current_key.lower():
                status = "lower"
            else:
                break
        else:
            if not ((status == "upper" and current_key == current_key.upper()) or
                    (status == "lower" and current_key == current_key.lower())):
                status = "mixed"
                break
            else:
                break

    return status == "upper" or status == "lower"