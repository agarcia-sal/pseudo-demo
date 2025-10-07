from typing import Sequence, Any

def cycpattern_check(param_one: Sequence[Any], param_two: Sequence[Any]) -> bool:
    while_step: int = 0
    roll_length: int = len(param_two)
    doubled_seq: Sequence[Any] = param_two + param_two  # concatenate to simulate rotation
    outer_done: bool = False

    while not outer_done:
        compare_limit: int = len(param_one) - roll_length
        break_flag: bool = False
        if while_step > compare_limit:
            outer_done = True
        else:
            inner_index: int = 0
            inner_limit: int = roll_length + 1
            inner_complete: bool = False
            while not inner_complete:
                if inner_index >= inner_limit:
                    inner_complete = True
                else:
                    main_slice = param_one[while_step : while_step + roll_length]
                    pattern_slice = doubled_seq[inner_index : inner_index + roll_length]
                    slices_match: bool = (main_slice == pattern_slice)
                    if slices_match:
                        break_flag = True
                        inner_complete = True
                        outer_done = True
                    inner_index += 1
        if break_flag:
            return True
        while_step += 1
    return False