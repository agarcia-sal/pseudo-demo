from typing import Any, Dict, Iterator


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    mode: str = "start"
    key_iterator: Iterator[Any] = iter(dictionary.keys())

    while True:
        try:
            current_key = next(key_iterator)
        except StopIteration:
            break

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key.isupper():
                mode = "upper"
            elif current_key.islower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and not current_key.isupper()) or (mode == "lower" and not current_key.islower()):
            mode = "mixed"
            break
        else:
            break

    return mode == "upper" or mode == "lower"