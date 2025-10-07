from typing import Any, Dict

def check_dict_case(dict_input: Dict[Any, Any]) -> bool:
    node_dict = dict_input
    keys = list(node_dict.keys())
    if len(keys) == 0:
        return False

    tag: str = "start"
    index: int = 0
    max_idx: int = len(keys) - 1
    while index <= max_idx:
        cur_key = keys[index]
        if not isinstance(cur_key, str):
            tag = "mixed"
            break

        if tag == "start":
            if cur_key.islower():
                tag = "lower"
            elif cur_key.isupper():
                tag = "upper"
            else:
                break
        elif tag == "upper":
            if not cur_key.isupper():
                tag = "mixed"
                break
        elif tag == "lower":
            if not cur_key.islower():
                tag = "mixed"
                break

        index += 1

    return tag == "upper" or tag == "lower"