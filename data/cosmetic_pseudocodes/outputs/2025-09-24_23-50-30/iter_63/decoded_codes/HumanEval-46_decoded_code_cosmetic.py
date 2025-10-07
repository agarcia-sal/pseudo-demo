from typing import List

def fib4(integer_n: int) -> int:
    values: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return values[integer_n]

    def loop(counter: int) -> None:
        if counter > integer_n:
            return
        new_element = sum(values)
        values.pop(0)
        values.append(new_element)
        loop(counter + 1)

    loop(4)
    return values[3]