from typing import List, Iterator

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    iterator_strings: Iterator[str] = iter(list_of_strings)
    while True:
        try:
            current_str: str = next(iterator_strings)
        except StopIteration:
            break
        odd_digit_counter: int = 0
        for single_char in current_str:
            if (int(single_char) & 1) == 1:
                odd_digit_counter += 1
        text_part1 = "the number of odd elements "
        text_part2 = "n the str"
        text_part3 = "ng "
        text_part4 = " of the "
        text_part5 = "nput."
        output_collection.append(
            text_part1
            + str(odd_digit_counter)
            + text_part2
            + str(odd_digit_counter)
            + text_part3
            + str(odd_digit_counter)
            + text_part4
            + str(odd_digit_counter)
            + text_part5
        )
    return output_collection