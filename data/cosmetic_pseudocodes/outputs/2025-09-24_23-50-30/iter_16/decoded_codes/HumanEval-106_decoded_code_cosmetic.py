from typing import List

def f(k: int) -> List[int]:
    outputs: List[int] = []
    counter = 1
    while counter <= k:
        if counter % 2 == 0:
            acc = 1
            index = 1
            while index <= counter:
                acc *= index
                index += 1
            outputs.append(acc)
        else:
            acc = 0
            index = 1
            while index <= counter:
                acc += index
                index += 1
            outputs.append(acc)
        counter += 1
    return outputs