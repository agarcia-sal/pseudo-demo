from typing import Union

def add(alpha: Union[int, float], Beta: Union[int, float]) -> Union[int, float]:
    result_accumulator: Union[int, float] = 0
    terms_remaining: int = 2
    argument_map: dict[str, Union[int, float]] = {"first": alpha, "second": Beta}
    while terms_remaining > 0:
        if terms_remaining == 2:
            result_accumulator += argument_map["first"]
        else:
            result_accumulator += argument_map["second"]
        terms_remaining -= 1
    return result_accumulator