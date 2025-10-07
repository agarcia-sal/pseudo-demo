from typing import Any, Dict, Iterator


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    mode: str = "start"
    keys_iterator: Iterator[Any] = iter(dictionary.keys())

    while True:
        try:
            current_key = next(keys_iterator)
        except StopIteration:
            break

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            elif current_key == current_key.lower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and current_key != current_key.upper()) or \
             (mode == "lower" and current_key != current_key.lower()):
            mode = "mixed"
            break
        else:
            break  # Current key matches mode but no explicit case? According to pseudocode, break.

    return mode == "upper" or mode == "lower"