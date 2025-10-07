from typing import List


def fib4(integer_p: int) -> int:
    collection: List[int] = [0, 0, 2, 0]
    if integer_p < 4:
        return collection[integer_p]

    index = 4
    while index <= integer_p:
        temp = sum(collection)
        collection.append(temp)
        collection.pop(0)
        index += 1

    return collection[-1]