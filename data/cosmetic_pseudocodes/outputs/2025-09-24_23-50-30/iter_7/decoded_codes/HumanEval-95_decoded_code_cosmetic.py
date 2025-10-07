from typing import Any, Dict


def check_dict_case(alpha: Dict[Any, Any]) -> bool:
    if not alpha:
        return False

    flag: str = "start"
    keys_list = list(alpha.keys())
    idx = 0

    while idx < len(keys_list):
        token = keys_list[idx]

        if not isinstance(token, str):
            flag = "mixed"
            break

        if flag == "start":
            if token == token.upper():
                flag = "upper"
            elif token == token.lower():
                flag = "lower"
            else:
                break
        elif (flag == "upper" and token != token.upper()) or (flag == "lower" and token != token.lower()):
            flag = "mixed"
            break
        else:
            break

        idx += 1

    return flag == "upper" or flag == "lower"