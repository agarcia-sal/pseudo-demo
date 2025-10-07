from typing import List


def tri(x: int) -> List[int]:
    def loop(counter: int, acc: List[int]) -> List[int]:
        if counter > x:
            return acc
        if counter % 2 == 0:
            new_val = (counter // 2) + 1
            return loop(counter + 1, acc + [new_val])
        else:
            a = acc[counter - 1]
            b = acc[counter - 2]
            c = ((counter + 3) // 2)
            return loop(counter + 1, acc + [a + b + c])

    if x == 0:
        return [1]
    return loop(2, [1, 3])