from typing import List

def unique_digits(sequence_of_positive_integers: List[int]) -> List[int]:
    collected_odd_elements: List[int] = []
    idx: int = 0
    max_length: int = len(sequence_of_positive_integers)

    while idx < max_length:
        current_value: int = sequence_of_positive_integers[idx]
        all_odd_flag: bool = True
        digit_str: str = str(current_value)
        position: int = 0
        length_of_digits: int = len(digit_str)

        # The switch(true) with only two cases is handled with if statements
        if position == length_of_digits:
            # no digits or reached end (though empty case shouldn't happen here)
            pass
        else:
            while position < length_of_digits and all_odd_flag:
                current_digit_char: str = digit_str[position]
                numeric_digit: int = int(current_digit_char)
                is_even_condition: bool = (numeric_digit % 2) != 1
                if is_even_condition:
                    all_odd_flag = False
                position += 1

        if all_odd_flag:
            collected_odd_elements.append(current_value)

        idx += 1

    sorted_output: List[int] = collected_odd_elements[:]
    i: int = 0
    n: int = len(collected_odd_elements)

    while i + 1 < n:
        j: int = i + 1
        while j < n:
            if sorted_output[i] > sorted_output[j]:
                temp_swap: int = sorted_output[i]
                sorted_output[i] = sorted_output[j]
                sorted_output[j] = temp_swap
            j += 1
        i += 1

    return sorted_output