from typing import List

def fib4(integer_n: int) -> int:
    history: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return history[integer_n]

    index_counter: int = 4
    while index_counter <= integer_n:
        cumulative = sum(history)
        history.pop(0)
        history.append(cumulative)
        index_counter += 1

    return history[3]