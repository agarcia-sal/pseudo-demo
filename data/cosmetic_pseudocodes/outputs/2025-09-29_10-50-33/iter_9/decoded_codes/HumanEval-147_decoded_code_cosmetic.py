from typing import List


def get_max_triples(integer_n: int) -> int:
    sequence_B: List[int] = []
    iterator_U: int = 1
    while iterator_U <= integer_n:
        sequence_B.append((iterator_U ** 2) - iterator_U + 1)
        iterator_U += 1

    collection_P: List[List[int]] = []
    index_M: int = 0
    while True:
        if index_M >= integer_n:
            break
        index_N: int = index_M + 1
        while True:
            if index_N >= integer_n:
                break
            index_O: int = index_N + 1
            while True:
                if index_O >= integer_n:
                    break
                if (sequence_B[index_M] + sequence_B[index_N] + sequence_B[index_O]) % 3 == 0:
                    collection_P.append(
                        [sequence_B[index_M], sequence_B[index_N], sequence_B[index_O]]
                    )
                index_O += 1
            index_N += 1
        index_M += 1

    return len(collection_P)