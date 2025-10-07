from typing import Any


def check_dict_case(dict_arg: dict[Any, Any]) -> bool:
    keys_list = list(dict_arg.keys())
    keys_count = len(keys_list)
    if keys_count == 0:
        return False

    mode: str = "start"
    index: int = 0

    while index < keys_count:
        current_key = keys_list[index]
        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key.isupper():
                mode = "upper"
            elif current_key.islower():
                mode = "lower"
            else:
                break  # key is string but neither all upper nor all lower
        elif mode == "upper" and not current_key.isupper():
            mode = "mixed"
            break
        elif mode == "lower" and not current_key.islower():
            mode = "mixed"
            break
        elif mode not in ("upper", "lower"):
            break

        index += 1

    return mode == "upper" or mode == "lower"