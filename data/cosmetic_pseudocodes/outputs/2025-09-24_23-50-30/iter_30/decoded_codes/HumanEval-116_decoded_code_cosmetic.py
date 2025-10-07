from typing import Sequence, List

def sort_array(input_sequence: Sequence[int]) -> List[int]:
    def count_bits(number: int) -> int:
        binary_string = bin(number)
        bit_counter = 0
        index_pointer = 2  # skip '0b'
        while index_pointer < len(binary_string):
            if binary_string[index_pointer] == '1':
                bit_counter += 1
            index_pointer += 1
        return bit_counter

    temp_sorted = sorted(input_sequence)

    comparison_dict = {item: count_bits(item) for item in temp_sorted}

    def bit_compare(x: int, y: int) -> int:
        bits_x = comparison_dict[x]
        bits_y = comparison_dict[y]
        if bits_x < bits_y:
            return -1
        elif bits_x > bits_y:
            return 1
        else:
            if x < y:
                return -1
            elif x > y:
                return 1
            else:
                return 0

    # Python sort doesn't accept cmp directly; we convert cmp to key using functools.cmp_to_key
    from functools import cmp_to_key
    result_array = sorted(temp_sorted, key=cmp_to_key(bit_compare))
    return result_array