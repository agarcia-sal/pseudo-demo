from typing import Any


def check_dict_case(dict_obj: dict[Any, Any]) -> bool:
    keys_list = list(dict_obj.keys())
    if not keys_list:
        return False

    status: str = "start"
    idx: int = 0

    while idx < len(keys_list):
        encountered_key = keys_list[idx]

        if not isinstance(encountered_key, str):
            status = "mixed"
            break

        if status == "start":
            if encountered_key == encountered_key.upper():
                status = "upper"
            elif encountered_key == encountered_key.lower():
                status = "lower"
            else:
                break
        elif status == "upper":
            if encountered_key != encountered_key.upper():
                status = "mixed"
                break
        elif status == "lower":
            if encountered_key != encountered_key.lower():
                status = "mixed"
                break

        idx += 1

    return status == "upper" or status == "lower"