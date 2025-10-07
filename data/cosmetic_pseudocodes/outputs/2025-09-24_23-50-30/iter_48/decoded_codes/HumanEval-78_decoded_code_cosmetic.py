from typing import List

def hex_key(param_one: List[str]) -> int:
    prime_list: List[str] = ['D', '7', '5', 'B', '3', '2']
    accumulator: int = 0

    idx: int = 0
    while idx <= len(param_one) - 1:
        if not (param_one[idx] == prime_list[0] or
                param_one[idx] == prime_list[1] or
                param_one[idx] == prime_list[2] or
                param_one[idx] == prime_list[3] or
                param_one[idx] == prime_list[4] or
                param_one[idx] == prime_list[5]):
            break
        else:
            accumulator += 1
        idx += 1

    return accumulator