from typing import Union

def how_many_times(input_value: Union[str, list], search_value: Union[str, list]) -> int:
    match_tally: int = 0
    limit_index: int = len(input_value) - len(search_value)

    def loop(i: int) -> None:
        nonlocal match_tally
        if i > limit_index:
            return
        else:
            # substring equality check
            if not (input_value[i:i + len(search_value)] != search_value):
                match_tally += 1
            loop(i + 1)

    loop(0)
    return match_tally