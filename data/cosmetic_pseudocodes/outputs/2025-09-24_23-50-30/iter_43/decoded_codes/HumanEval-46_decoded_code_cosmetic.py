from typing import List

def fib4(integer_a: int) -> int:
    collection_b: List[int] = [0, 0, 2, 0]
    if integer_a < 4:
        return collection_b[integer_a]

    index_c: int = 4
    while index_c <= integer_a:
        sum_d: int = sum(collection_b)
        collection_b[0], collection_b[1], collection_b[2], collection_b[3] = (
            collection_b[1],
            collection_b[2],
            collection_b[3],
            sum_d,
        )
        index_c += 1

    return collection_b[3]