from collections import deque
from typing import List


def f(integer_n: int) -> List[int]:
    output_queue: deque[int] = deque()
    index_p: int = 1

    while index_p <= integer_n:
        temp_num: int = index_p
        cond_flag: bool = (temp_num % 2) == 0  # True if even, False if odd

        if not cond_flag:
            accum_sum: int = 0
            counter_q: int = 1
            while counter_q <= temp_num:
                accum_sum += counter_q
                counter_q += 1
            output_queue.append(accum_sum)
        else:
            accum_product: int = 1
            counter_q: int = 1
            while counter_q != temp_num:
                accum_product *= counter_q
                counter_q += 1
            accum_product *= counter_q  # multiply by temp_num itself
            output_queue.append(accum_product)

        index_p += 1

    final_result: List[int] = []
    while output_queue:
        final_result.append(output_queue.popleft())

    return final_result