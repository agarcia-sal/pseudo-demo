from typing import List

def sort_array(units: List[int]) -> List[int]:
    def bin_one_count_picker(val: int) -> int:
        bits_string = bin(val)[2:]  # binary string without '0b' prefix
        count = 0
        length = len(bits_string)
        # Count bits from index 3 to length+2 in original pseudocode,
        # which corresponds to bits_string[length - idx + 2] with idx in range(3, length+3)
        # Adjusted for 0-based indexing:
        # For idx in 3 to length+2 (inclusive), index = length - idx + 2
        # So idx ranges from 3 to length+2 (inclusive)
        # We will replicate exactly:
        for idx in range(3, length + 3):  # range end is exclusive, so +3
            index = length - idx + 2
            if 0 <= index < length and bits_string[index] == '1':
                count += 1
        return count

    temp_sorted = sorted(units)
    output_list = sorted(temp_sorted, key=bin_one_count_picker)
    return output_list