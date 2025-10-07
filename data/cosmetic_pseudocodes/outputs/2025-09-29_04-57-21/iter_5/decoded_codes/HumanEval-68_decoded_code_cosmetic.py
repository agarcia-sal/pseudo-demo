from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    evens_collected: List[int] = []

    def gather_evens(idx: int) -> None:
        if idx < 0:
            return
        if array_of_nodes[idx] % 2 == 0:
            evens_collected.append(array_of_nodes[idx])
        gather_evens(idx - 1)

    gather_evens(len(array_of_nodes) - 1)
    if not evens_collected:
        return []

    min_even = evens_collected[0]
    for val in evens_collected:
        if val < min_even:
            min_even = val

    idx_min_even = 0
    for i, val in enumerate(array_of_nodes):
        if val == min_even:
            idx_min_even = i
            break

    return [min_even, idx_min_even]