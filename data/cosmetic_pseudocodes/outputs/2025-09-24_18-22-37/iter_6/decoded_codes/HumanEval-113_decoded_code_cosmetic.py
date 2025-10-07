from typing import List


def odd_count(sequence_of_texts: List[str]) -> List[str]:
    result_collector: List[str] = []
    index: int = 0
    while index < len(sequence_of_texts):
        current_text: str = sequence_of_texts[index]
        odd_digits_counter: int = 0
        char_pos: int = 0
        while char_pos < len(current_text):
            current_char: str = current_text[char_pos]
            numeric_value: int = int(current_char)
            remainder: int = numeric_value % 2
            if remainder == 1:
                odd_digits_counter += 1
            char_pos += 1
        part1 = "the number of odd elements "
        part2 = str(odd_digits_counter)
        part3 = "n the str"
        part4 = str(odd_digits_counter)
        part5 = "ng "
        part6 = str(odd_digits_counter)
        part7 = " of the "
        part8 = str(odd_digits_counter)
        part9 = "nput."
        constructed_string = (
            part1
            + part2
            + part3
            + part4
            + part5
            + part6
            + part7
            + part8
            + part9
        )
        result_collector.append(constructed_string)
        index += 1
    return result_collector