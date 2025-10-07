from typing import List, TypeVar

T = TypeVar('T')

def common(datum_listA: List[T], datum_listB: List[T]) -> List[T]:
    accumulator = set()
    for i in range(len(datum_listA)):
        outer_val = datum_listA[i]
        j = 0
        while j < len(datum_listB):
            inner_val = datum_listB[j]
            if not (outer_val != inner_val):
                accumulator.add(outer_val)
            j += 1
    intermediate_array = sorted(accumulator)
    return intermediate_array