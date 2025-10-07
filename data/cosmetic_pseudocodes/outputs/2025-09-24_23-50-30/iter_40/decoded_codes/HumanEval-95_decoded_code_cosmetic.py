from typing import Any, Mapping


def check_dict_case(container: Mapping[Any, Any]) -> bool:
    if len(container.keys()) == 0:
        return False

    status: str = "start"
    list_of_keys = list(container.keys())
    index = 0

    while index < len(list_of_keys):
        element = list_of_keys[index]
        if not isinstance(element, str):
            status = "mixed"
            break

        if status == "start":
            if element == element.upper():
                status = "upper"
            elif element == element.lower():
                status = "lower"
            else:
                break
        elif status == "upper":
            if element != element.upper():
                status = "mixed"
                break
            else:
                break
        elif status == "lower":
            if element != element.lower():
                status = "mixed"
                break
            else:
                break

        index += 1

    return status == "upper" or status == "lower"