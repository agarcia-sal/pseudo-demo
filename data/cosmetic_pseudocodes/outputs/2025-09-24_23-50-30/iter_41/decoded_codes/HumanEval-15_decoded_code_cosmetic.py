from typing import List


def string_sequence(integer_z: int) -> str:
    collection_a: List[str] = []
    index_b: int = 0
    while True:
        if index_b > integer_z:
            break
        collection_a.append(str(index_b))
        index_b += 1
    return " ".join(collection_a)