from typing import List, Tuple

def get_max_triples(integer_n: int) -> int:
    list_A: List[int] = [(i * i - i + 1) for i in range(1, integer_n + 1)]
    list_ans: List[Tuple[int, int, int]] = []
    for i in range(integer_n - 2):
        ai = list_A[i]
        for j in range(i + 1, integer_n - 1):
            aj = list_A[j]
            for k in range(j + 1, integer_n):
                ak = list_A[k]
                if (ai + aj + ak) % 3 == 0:
                    list_ans.append((ai, aj, ak))
    return len(list_ans)