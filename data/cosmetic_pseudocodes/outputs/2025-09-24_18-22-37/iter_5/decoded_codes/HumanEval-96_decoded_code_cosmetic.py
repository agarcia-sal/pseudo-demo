from typing import List

def count_up_to(parameter: int) -> List[int]:
    result_list: List[int] = []
    outer_index: int = 2
    while outer_index < parameter:
        prime_flag: bool = True
        inner_index: int = 2
        while inner_index < outer_index:
            remainder = outer_index - ((outer_index // inner_index) * inner_index)
            if remainder == 0:
                prime_flag = False
                break
            else:
                inner_index += 1
        if prime_flag:
            result_list.append(outer_index)
        outer_index += 1
    return result_list