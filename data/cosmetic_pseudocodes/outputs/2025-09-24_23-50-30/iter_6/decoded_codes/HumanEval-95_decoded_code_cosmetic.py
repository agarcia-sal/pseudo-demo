from typing import Mapping, Any

def check_dict_case(collection: Mapping[Any, Any]) -> bool:
    keys_list = list(collection.keys())
    if not keys_list:
        return False

    mode: str = "start"
    index: int = 0

    while index < len(keys_list):
        current_item = keys_list[index]

        if not isinstance(current_item, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_item.upper() == current_item:
                mode = "upper"
            else:
                if current_item.lower() == current_item:
                    mode = "lower"
                else:
                    break
        elif mode == "upper":
            if current_item.upper() != current_item:
                mode = "mixed"
                break
        elif mode == "lower":
            if current_item.lower() != current_item:
                mode = "mixed"
                break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"