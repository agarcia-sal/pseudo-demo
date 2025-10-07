from typing import Sequence, List


def sort_array(input_sequence: Sequence[int]) -> List[int]:
    intermediate_collection: List[int] = sorted(input_sequence)

    def count_ones_in_binary(number: int) -> int:
        binary_string = bin(number)
        # Count '1's in binary string starting from index 3 per pseudocode (skipping '0b' + one char)
        return sum(1 for c in binary_string[3:] if c == '1')

    result_sequence: List[int] = sorted(intermediate_collection, key=count_ones_in_binary)
    return result_sequence