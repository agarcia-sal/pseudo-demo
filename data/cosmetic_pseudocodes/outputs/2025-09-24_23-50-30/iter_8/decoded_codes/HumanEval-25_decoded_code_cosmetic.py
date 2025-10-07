from typing import List


def factorize(integer_n: int) -> List[int]:
    result_collection: List[int] = []
    candidate: int = 2
    while True:
        if candidate * candidate > integer_n:
            break
        if integer_n % candidate == 0:
            result_collection.append(candidate)
            integer_n //= candidate
        else:
            candidate += 1
    if integer_n > 1:
        result_collection.append(integer_n)
    return result_collection