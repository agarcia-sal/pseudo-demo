from typing import List


def make_a_pile(integer_q: int) -> List[int]:
    collection: List[int] = []
    counter: int = 0
    while True:
        if counter >= integer_q:
            break
        temp: int = 2 * counter
        element: int = integer_q + temp
        collection.append(element)
        counter += 1
    return collection