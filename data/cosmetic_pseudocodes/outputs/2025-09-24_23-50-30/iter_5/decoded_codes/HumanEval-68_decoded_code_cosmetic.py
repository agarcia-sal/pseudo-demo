from typing import List, Union


def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    def find_even_subset(collection: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx >= len(collection):
            return acc
        current_val = collection[idx]
        if current_val % 2 == 0:
            return find_even_subset(collection, idx + 1, acc + [current_val])
        else:
            return find_even_subset(collection, idx + 1, acc)

    evens = find_even_subset(array_of_nodes, 0, [])

    if len(evens) == 0:
        return []
    else:
        min_even = evens[0]
        for i in range(1, len(evens)):
            if evens[i] < min_even:
                min_even = evens[i]

        pos = 0
        for j in range(len(array_of_nodes)):
            if array_of_nodes[j] == min_even:
                pos = j
                break

        return [min_even, pos]