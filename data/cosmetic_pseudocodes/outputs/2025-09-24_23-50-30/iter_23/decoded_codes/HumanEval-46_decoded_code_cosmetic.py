from typing import List


def fib4(integer_n: int) -> int:
    queue: List[int] = [0, 0, 2, 0]

    if integer_n > 3:
        index = 4
        while index <= integer_n:
            total = sum(queue[1:5])  # sum positions 1 to 4 inclusive from queue
            queue.append(total)
            del queue[0]  # remove queue[1] in 1-based indexing corresponds to queue[0] in 0-based
            index += 1
        return queue[3]  # queue[4] in 1-based indexing
    else:
        return queue[integer_n + 1]