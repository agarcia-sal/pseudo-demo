from typing import List

def fib4(integer_n: int) -> int:
    def helper(queue_values: List[int], current_index: int) -> int:
        if current_index == integer_n:
            return queue_values[3]

        computed_value = sum(queue_values)
        updated_queue = [queue_values[1], queue_values[2], queue_values[3], computed_value]
        return helper(updated_queue, current_index + 1)

    if integer_n < 4:
        if integer_n == 0:
            return 0
        elif integer_n == 1:
            return 0
        elif integer_n == 2:
            return 2
        else:  # integer_n == 3
            return 0

    return helper([0, 0, 2, 0], 4)