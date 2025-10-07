from typing import Any, Dict


def check_dict_case(input_map: Dict[Any, Any]) -> bool:
    result_flag: bool = False
    key_collection = list(input_map.keys())
    if len(key_collection) == 0:
        result_flag = False
    else:
        status_marker: str = "start"
        index_counter: int = 0
        while index_counter < len(key_collection) and status_marker != "mixed":
            present_key = key_collection[index_counter]
            if not isinstance(present_key, str):
                status_marker = "mixed"
            else:
                if status_marker == "start":
                    if present_key.upper() == present_key:
                        status_marker = "upper"
                    else:
                        if present_key.lower() == present_key:
                            status_marker = "lower"
                        else:
                            index_counter = len(key_collection)  # force exit from loop
                else:
                    if (status_marker == "upper" and present_key.upper() != present_key) or \
                       (status_marker == "lower" and present_key.lower() != present_key):
                        status_marker = "mixed"
                    else:
                        index_counter = len(key_collection)  # force exit from loop
            index_counter += 1
        result_flag = (status_marker == "upper") or (status_marker == "lower")
    return result_flag