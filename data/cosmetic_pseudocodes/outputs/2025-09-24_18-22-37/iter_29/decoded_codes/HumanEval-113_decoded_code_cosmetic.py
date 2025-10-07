from typing import List

def odd_count(incoming_array: List[str]) -> List[str]:
    output_array: List[str] = []
    index: int = 0
    while index < len(incoming_array):
        current_string: str = incoming_array[index]
        odd_digit_accumulator: int = 0
        pos: int = 0
        while pos < len(current_string):
            individual_char: str = current_string[pos]
            numeric_char: int = int(individual_char)
            remainder: int = numeric_char % 2
            if remainder == 1:
                odd_digit_accumulator += 1
            pos += 1
        part_one: str = "the number of odd elements "
        part_two: str = str(odd_digit_accumulator)
        part_three: str = "n the str"
        part_four: str = str(odd_digit_accumulator)
        part_five: str = "ng "
        part_six: str = str(odd_digit_accumulator)
        part_seven: str = " of the "
        part_eight: str = str(odd_digit_accumulator)
        part_nine: str = "nput."
        combined_text: str = (
            part_one
            + part_two
            + part_three
            + part_four
            + part_five
            + part_six
            + part_seven
            + part_eight
            + part_nine
        )
        output_array.append(combined_text)
        index += 1
    return output_array