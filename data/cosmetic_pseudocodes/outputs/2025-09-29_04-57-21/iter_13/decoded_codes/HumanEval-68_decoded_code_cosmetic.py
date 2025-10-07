from typing import List, Tuple


def pluck(array_of_nodes: List[int]) -> List[int | int]:
    def find_even_numbers(collection: List[int], acc: List[int]) -> List[int]:
        if not collection:
            return acc
        head, *tail = collection
        if head % 2 == 0:
            return find_even_numbers(tail, acc + [head])
        else:
            return find_even_numbers(tail, acc)

    evens_list = find_even_numbers(array_of_nodes, [])
    if not evens_list:
        return []

    minimum_even = evens_list[0]
    for element in evens_list[1:]:
        if element < minimum_even:
            minimum_even = element

    original_position = -1
    pos = 0
    while pos < len(array_of_nodes):
        if array_of_nodes[pos] == minimum_even:
            original_position = pos
            break
        pos += 1

    return [minimum_even, original_position]