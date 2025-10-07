from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    # Extract even-indexed elements recursively
    def extract_even(
        lst: List[T], evens: List[T], odds: List[T], idx: int
    ) -> List[T]:
        if idx < len(lst) and idx % 2 == 0:
            evens.append(lst[idx])
            return extract_even(lst, evens, odds, idx + 1)
        return evens

    # Extract odd-indexed elements recursively
    def extract_odd(lst: List[T], odds: List[T], idx: int) -> List[T]:
        if idx < len(lst) and idx % 2 != 0:
            odds.append(lst[idx])
            return extract_odd(lst, odds, idx + 1)
        return odds

    evens: List[T] = []
    odds: List[T] = []

    evens = extract_even(list_of_elements, evens, odds, 0)
    odds = extract_odd(list_of_elements, odds, 1)

    sorted_evens = sorted(evens)

    # Rebuild list from sorted evens and original odds by interleaving
    def interleave(a: List[T], b: List[T]) -> List[T]:
        if not a or not b:
            return []
        return [a[0], b[0]] + interleave(a[1:], b[1:])

    interleaved = interleave(sorted_evens, odds)

    # If evens are longer than odds, append the last even element
    if len(sorted_evens) > len(odds):
        interleaved.append(sorted_evens[-1])

    return interleaved