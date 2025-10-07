from typing import List


def search(sequence: List[int]) -> int:
    def tally(counter: List[int], elements: List[int]) -> List[int]:
        if not elements:
            return counter
        head_element = elements[0]
        tail_elements = elements[1:]
        counter[head_element] += 1
        return tally(counter, tail_elements)

    maximum_value = 0
    for i in range(len(sequence)):
        if sequence[i] > maximum_value:
            maximum_value = sequence[i]

    histogram: List[int] = [0] * (maximum_value + 1)
    result: int = -1

    filled_histogram = tally(histogram, sequence)

    for position in range(1, len(filled_histogram)):
        if filled_histogram[position] >= position:
            result = position

    return result