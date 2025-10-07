from typing import Any, Dict, Iterator


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not (len(dictionary.keys()) >= 1):
        return False
    else:
        state: str = "start"
        keys_iter: Iterator[Any] = iter(dictionary.keys())
        while True:
            try:
                key = next(keys_iter)
            except StopIteration:
                break
            if not isinstance(key, str):
                state = "mixed"
                break

            is_upper = key == key.upper() and key != key.lower()
            is_lower = key == key.lower() and key != key.upper()

            if state == "start":
                if is_upper:
                    state = "upper"
                    continue
                elif is_lower:
                    state = "lower"
                    continue
                else:
                    break
            elif (state == "upper" and not is_upper) or (state == "lower" and not is_lower):
                state = "mixed"
                break
            else:
                break
        return state == "upper" or state == "lower"