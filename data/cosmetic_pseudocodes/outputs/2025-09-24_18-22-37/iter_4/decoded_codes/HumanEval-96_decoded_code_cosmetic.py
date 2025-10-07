from typing import List


def count_up_to(n: int) -> List[int]:
    result: List[int] = []
    outer_index: int = 2
    while outer_index < n:
        prime_flag: bool = True
        inner_index: int = 2
        while inner_index < outer_index:
            if outer_index % inner_index == 0:
                prime_flag = False
                inner_index = outer_index  # break inner loop
            else:
                inner_index += 1
        if prime_flag:
            result.append(outer_index)
        outer_index += 1
    return result