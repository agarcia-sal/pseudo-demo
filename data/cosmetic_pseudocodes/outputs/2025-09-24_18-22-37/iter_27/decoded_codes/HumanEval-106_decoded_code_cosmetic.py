from typing import List

def f(parameter_m: int) -> List[int]:
    collection_result: List[int] = []
    index_p: int = 1
    while index_p <= parameter_m:
        flag_even_check: int = index_p % 2
        if not (flag_even_check != 0):  # True if index_p is even
            temp_factorial: int = 1
            counter_r: int = 1
            while counter_r <= index_p:
                temp_factorial *= counter_r
                counter_r += 1
            collection_result.append(temp_factorial)
        else:
            temp_sum: int = 0
            counter_s: int = 1
            while counter_s <= index_p:
                temp_sum += counter_s
                counter_s += 1
            collection_result.append(temp_sum)
        index_p += 1
    return collection_result