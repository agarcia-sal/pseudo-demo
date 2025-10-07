from typing import List

def f(integer_n: int) -> List[int]:
    output: List[int] = []
    counter: int = 1
    while counter <= integer_n:
        if (counter % 2) == 0:
            fact: int = 1
            multiplier: int = 1
            while multiplier <= counter:
                fact *= multiplier
                multiplier += 1
            output.append(fact)
        else:
            sum_val: int = 0
            index: int = 1
            while index <= counter:
                sum_val += index
                index += 1
            output.append(sum_val)
        counter += 1
    return output