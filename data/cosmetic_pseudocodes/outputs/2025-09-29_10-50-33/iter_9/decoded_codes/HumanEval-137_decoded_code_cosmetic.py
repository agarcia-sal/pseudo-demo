from typing import Any, Optional


def compare_one(a: Any, b: Any) -> Optional[Any]:
    shadow_x: Any = a
    shadow_y: Any = b

    def normalize_string(input_val: Any) -> Any:
        if not isinstance(input_val, str):
            return input_val
        modified_val = input_val.replace(',', '.')
        return modified_val

    shadow_x = normalize_string(shadow_x)
    shadow_y = normalize_string(shadow_y)

    def to_num(entity: Any) -> float:
        return float(entity)

    first_num = to_num(shadow_x)
    second_num = to_num(shadow_y)

    if first_num == second_num:
        return None

    if not (second_num >= first_num):
        return a

    return b