from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulated_results: List[str] = []

    def count_odd_digits(text_line: str, position: int, total_odd: int) -> int:
        if position == len(text_line):
            return total_odd
        current_char = text_line[position]
        odd_increment = 1 if current_char.isdigit() and (int(current_char) % 2 == 1) else 0
        return count_odd_digits(text_line, position + 1, total_odd + odd_increment)

    def process_items(index: int) -> None:
        if index == len(list_of_strings):
            return
        current_string = list_of_strings[index]
        total_odd_count = count_odd_digits(current_string, 0, 0)
        accumulated_results.append(
            "the number of odd elements "
            + str(total_odd_count)
            + "n the str"
            + str(total_odd_count)
            + "ng "
            + str(total_odd_count)
            + " of the "
            + str(total_odd_count)
            + "nput."
        )
        process_items(index + 1)

    process_items(0)
    return accumulated_results