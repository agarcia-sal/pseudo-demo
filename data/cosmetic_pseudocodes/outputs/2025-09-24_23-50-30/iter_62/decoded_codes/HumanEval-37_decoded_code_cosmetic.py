from typing import List, TypeVar

T = TypeVar('T')

def sort_even(array_input: List[T]) -> List[T]:
    def interleave_recursive(seq_a: List[T], seq_b: List[T], acc_result: List[T]) -> List[T]:
        if not seq_a and not seq_b:
            return acc_result
        if not seq_a:
            return acc_result + seq_b
        if not seq_b:
            return acc_result + seq_a
        # Add first element of seq_a and seq_b to accumulator and recurse without them
        return interleave_recursive(seq_a[1:], seq_b[1:], acc_result + [seq_a[0], seq_b[0]])

    extracted_even = [val for idx, val in enumerate(array_input) if idx % 2 == 0]
    extracted_odd = [val for idx, val in enumerate(array_input) if idx % 2 != 0]
    sorted_even = sorted(extracted_even)
    return interleave_recursive(sorted_even, extracted_odd, [])