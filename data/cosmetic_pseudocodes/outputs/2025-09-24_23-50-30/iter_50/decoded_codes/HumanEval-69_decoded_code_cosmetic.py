from functools import reduce
from typing import List


def search(list_of_integers: List[int]) -> int:
    def tally_frequencies(iterator: List[int], counts: List[int]) -> List[int]:
        if not iterator:
            return counts
        head, *tail = iterator
        previous_value = counts[head]
        # create updated counts list with incremented frequency at position 'head'
        updated_counts = counts[:head] + [previous_value + 1] + counts[head + 1 :]
        return tally_frequencies(tail, updated_counts)

    maximal_value = reduce(lambda a, b: a if a > b else b, list_of_integers) + 1
    initial_counts = [0] * maximal_value
    frequencies = tally_frequencies(list_of_integers, initial_counts)

    result_candidate = -1
    position_index = 1
    while position_index < len(frequencies):
        current_frequency = frequencies[position_index]
        if not (current_frequency < position_index):
            result_candidate = position_index
        position_index += 1

    return result_candidate