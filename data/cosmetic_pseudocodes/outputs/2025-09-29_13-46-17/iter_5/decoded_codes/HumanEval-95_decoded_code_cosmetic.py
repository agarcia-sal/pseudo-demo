from typing import Any, Dict, Iterator

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    dictionary_keys: Iterator[Any] = iter(dictionary.keys())

    try:
        first_key = next(dictionary_keys)
    except StopIteration:
        return False

    _state: str = "start"

    def inner_loop() -> None:
        nonlocal _state
        try:
            current_key = next(dictionary_keys)
        except StopIteration:
            return

        if not isinstance(current_key, str):
            _state = "mixed"
            return

        if _state == "start":
            if current_key.upper() == current_key:
                _state = "upper"
            elif current_key.lower() == current_key:
                _state = "lower"
            else:
                return
        elif (_state == "upper" and current_key.upper() != current_key) or (_state == "lower" and current_key.lower() != current_key):
            _state = "mixed"
            return
        else:
            return

        inner_loop()

    # Evaluate the first key outside to initialize _state properly
    if not isinstance(first_key, str):
        return False
    if first_key.upper() == first_key:
        _state = "upper"
    elif first_key.lower() == first_key:
        _state = "lower"
    else:
        return False

    inner_loop()
    return _state == "upper" or _state == "lower"