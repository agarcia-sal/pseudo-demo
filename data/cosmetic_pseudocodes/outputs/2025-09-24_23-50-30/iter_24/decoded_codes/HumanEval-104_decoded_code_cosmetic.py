from typing import List

def unique_digits(mutable_sequence_of_natural_numbers: List[int]) -> List[int]:
    transient_collection: List[int] = []
    aux_idx: int = 0  # zero-based index for Python list access

    while aux_idx < len(mutable_sequence_of_natural_numbers):
        helper_variable: str = str(mutable_sequence_of_natural_numbers[aux_idx])
        digit_check_flag: bool = True
        sub_index: int = 0  # zero-based index for string access

        while sub_index < len(helper_variable) and digit_check_flag:
            if (int(helper_variable[sub_index]) % 2) == 0:
                digit_check_flag = False
            sub_index += 1

        if digit_check_flag:
            transient_collection.append(mutable_sequence_of_natural_numbers[aux_idx])

        aux_idx += 1

    return sorted(transient_collection)