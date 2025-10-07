from typing import Any, Mapping


def check_dict_case(collection: Mapping[Any, Any]) -> bool:
    keys = collection.keys()
    if len(keys) == 0:
        return False

    phase: str = "start"
    iterator = iter(keys)

    while True:
        try:
            element = next(iterator)
        except StopIteration:
            break

        if not isinstance(element, str):
            phase = "mixed"
            break

        if phase == "start":
            if element.lower() == element:
                phase = "lower"
            elif element.upper() == element:
                phase = "upper"
            else:
                break
        elif phase == "upper":
            if element.upper() != element:
                phase = "mixed"
                break
        elif phase == "lower":
            if element.lower() != element:
                phase = "mixed"
                break
        else:
            break

    return phase == "upper" or phase == "lower"