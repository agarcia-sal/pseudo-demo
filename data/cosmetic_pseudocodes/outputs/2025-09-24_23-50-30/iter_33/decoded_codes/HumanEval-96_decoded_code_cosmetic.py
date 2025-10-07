from typing import List

def count_up_to(limit: int) -> List[int]:
    collected: List[int] = []
    outer_index: int = 2
    while outer_index < limit:
        prime_flag: bool = True
        inner_index: int = 2
        while inner_index < outer_index and prime_flag:
            if outer_index % inner_index == 0:
                prime_flag = False
            inner_index += 1
        if prime_flag:
            collected.append(outer_index)
        outer_index += 1
    return collected