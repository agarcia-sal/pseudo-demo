from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulated_result: List[str] = []

    def process_element(index_counter: int) -> None:
        if index_counter >= len(list_of_strings):
            return
        string_candidate: str = list_of_strings[index_counter]

        def compute_odd_character_count(char_index: int, accumulator: int) -> int:
            if char_index == len(string_candidate):
                return accumulator
            current_character: str = string_candidate[char_index]
            digit_value: int = int(current_character)
            updated_accumulator: int = accumulator + (1 * ((digit_value & 1) == 1))
            return compute_odd_character_count(char_index + 1, updated_accumulator)

        odd_digit_total: int = compute_odd_character_count(0, 0)
        appended_text: str = (
            "the number of odd elements "
            + str(odd_digit_total)
            + "n the str"
            + str(odd_digit_total)
            + "ng "
            + str(odd_digit_total)
            + " of the "
            + str(odd_digit_total)
            + "nput."
        )
        accumulated_result.append(appended_text)
        process_element(index_counter + 1)

    process_element(0)
    return accumulated_result