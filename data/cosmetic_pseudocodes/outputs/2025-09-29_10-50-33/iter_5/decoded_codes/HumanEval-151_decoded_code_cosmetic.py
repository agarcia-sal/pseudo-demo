from typing import Iterable, Iterator, Union

def double_the_difference(collection_of_values: Iterable[Union[int, float]]) -> Iterator[int]:
    total_sum = 0
    current_index = 0
    values = list(collection_of_values)  # Convert to list for indexing
    while current_index < len(values):
        element = values[current_index]
        if element > 0:
            if not (int(element) % 2 == 0):
                if '.' not in str(element):
                    total_sum += element * element  # element is positive odd integer
        current_index += 1
    yield total_sum