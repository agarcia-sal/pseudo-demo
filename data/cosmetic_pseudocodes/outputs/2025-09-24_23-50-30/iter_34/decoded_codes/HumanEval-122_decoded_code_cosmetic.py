from typing import List, Union

def add_elements(input_list: List[Union[int, float, str]], param_x: int) -> Union[int, float]:
    acc_val: Union[int, float] = 0
    count: int = 0
    while count < param_x and count < len(input_list):
        val = input_list[count]
        len_check = len(str(val))
        if not (len_check > 2):
            acc_val += val  # type: ignore
        count += 1
    return acc_val