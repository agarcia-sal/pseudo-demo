from typing import List, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def sort_even(list_of_elements: List[T]) -> List[T]:
    n = len(list_of_elements)
    if n % 2 != 0:
        # Collect elements at even indices except possibly the last odd index element
        evens = []
        for i in range(0, n, 2):
            if i == n - 1:
                evens.append(list_of_elements[i])
    else:
        evens = []
    # In the pseudocode, evens are folded left but only used at last element, above code matches

    # Collect elements at odd indices in original order via fold_right on reversed indices
    odds = [list_of_elements[i] for i in range(n - 1, -1, -1) if i % 2 == 1]
    odds.reverse()  # fold_right preserves original order of these elements

    def insert_sorted(x: T, sorted_list: List[T]) -> List[T]:
        # Insert x into sorted_list preserving sorted order ascending
        for idx, val in enumerate(sorted_list):
            if x <= val:
                return sorted_list[:idx] + [x] + sorted_list[idx:]
        return sorted_list + [x]

    def recur_sort(lst: List[T]) -> List[T]:
        if not lst:
            return []
        head, *tail = lst
        return insert_sorted(head, recur_sort(tail))

    sorted_evens = recur_sort(evens)

    result: List[T] = []
    for e, o in zip(sorted_evens, odds):
        result.extend([e, o])

    # If leftover element from sorted_evens exists, append it
    if len(sorted_evens) + len(odds) > 0:
        if len(sorted_evens) > len(odds):
            result.append(sorted_evens[-1])

    return result