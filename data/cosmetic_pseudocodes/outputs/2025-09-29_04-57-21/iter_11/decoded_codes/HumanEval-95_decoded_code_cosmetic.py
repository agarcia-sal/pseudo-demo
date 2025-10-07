from typing import Mapping, Any


def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    if len(mapping) == 0:
        return False

    status: str = "start"
    keys_list = list(mapping.keys())
    total_keys = len(keys_list)

    iterator = 0
    while iterator < total_keys:
        current_key = keys_list[iterator]

        if not isinstance(current_key, str):
            status = "mixed"
            break

        if status == "start":
            if current_key.isupper():
                status = "upper"
            elif current_key.islower():
                status = "lower"
            else:
                break
        elif (status == "upper" and not current_key.isupper()) or (status == "lower" and not current_key.islower()):
            status = "mixed"
            break
        else:
            break

        iterator += 1

    return status == "upper" or status == "lower"