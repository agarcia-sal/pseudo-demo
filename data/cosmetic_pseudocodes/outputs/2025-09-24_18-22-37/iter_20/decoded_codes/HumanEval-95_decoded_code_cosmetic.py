from typing import Mapping, Any


def is_string_all_upper(s: str) -> bool:
    for ch in s:
        if not ('A' <= ch <= 'Z'):
            return False
    return True


def is_string_all_lower(s: str) -> bool:
    for ch in s:
        if not ('a' <= ch <= 'z'):
            return False
    return True


def check_dict_case(container: Mapping[Any, Any]) -> bool:
    length_of_keys: int = 0
    for _ in container.keys():
        length_of_keys += 1

    if length_of_keys == 0:
        return False

    status: str = "start"
    iterator: int = 0
    keys_list = list(container.keys())

    while iterator < length_of_keys:
        element = keys_list[iterator]

        if not isinstance(element, str):
            status = "mixed"
            break

        key_type_correct = False

        if status == "start":
            is_uppercase_key = True
            is_lowercase_key = True
            for c in element:
                if not ('A' <= c <= 'Z'):
                    is_uppercase_key = False
                if not ('a' <= c <= 'z'):
                    is_lowercase_key = False

            if is_uppercase_key:
                status = "upper"
                key_type_correct = True
            elif is_lowercase_key:
                status = "lower"
                key_type_correct = True

            if not key_type_correct:
                break
        else:
            if (status == "upper" and not is_string_all_upper(element)) or (
                status == "lower" and not is_string_all_lower(element)
            ):
                status = "mixed"
                break
            elif status not in ("upper", "lower"):
                break

        iterator += 1

    if status == "upper" or status == "lower":
        return True
    else:
        return False