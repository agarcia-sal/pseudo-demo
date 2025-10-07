from collections import deque
from typing import List


def tri(integer_n: int) -> List[int]:
    result_queue: deque[int] = deque()
    if integer_n <= 0:
        result_queue.append(1)
        return list(result_queue)

    result_queue = deque([1, 3])
    loop_counter: int = 2

    while loop_counter <= integer_n:
        condition_flag: bool = (loop_counter % 2 == 0)

        if condition_flag:
            # integer division is appropriate here to get int result
            result_queue.append((loop_counter // 2) + 1)
        else:
            prev_val1: int = list(result_queue)[loop_counter - 1]
            prev_val2: int = list(result_queue)[loop_counter - 2]
            result_queue.append(prev_val1 + prev_val2 + ((loop_counter + 3) // 2))

        loop_counter += 1

    return list(result_queue)