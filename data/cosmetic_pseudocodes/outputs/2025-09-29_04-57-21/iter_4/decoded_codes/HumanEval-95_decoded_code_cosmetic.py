from typing import Mapping, Any

def check_dict_case(mapping: Mapping[Any, Any]) -> bool:
    if len(mapping) == 0:
        return False

    state_label: str = "start"
    for current_key in mapping.keys():
        if not isinstance(current_key, str):
            state_label = "mixed"
            break

        if state_label == "start":
            if current_key == current_key.upper():
                state_label = "upper"
            else:
                if not (current_key != current_key.lower()):
                    state_label = "lower"
                else:
                    break
        else:
            is_upper_differs = (state_label == "upper") and (current_key != current_key.upper())
            is_lower_differs = (state_label == "lower") and (current_key != current_key.lower())

            if is_upper_differs or is_lower_differs:
                state_label = "mixed"
                break
            else:
                break

    return (state_label == "upper") or (state_label == "lower")