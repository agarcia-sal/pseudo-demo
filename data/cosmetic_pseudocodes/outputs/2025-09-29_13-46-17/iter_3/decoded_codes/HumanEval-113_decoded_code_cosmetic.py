from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    def count_odd_chars(str_val: str, idx: int, accum: int) -> int:
        if idx == len(str_val):
            return accum
        current_char_value = int(str_val[idx])
        incremented_accum = accum + (1 if current_char_value % 2 == 1 else 0)
        return count_odd_chars(str_val, idx + 1, incremented_accum)

    results_collector: List[str] = []
    current_index: int = 0

    while current_index < len(list_of_strings):
        current_string = list_of_strings[current_index]
        odd_digits_count = count_odd_chars(current_string, 0, 0)
        message_parts = [
            "the number of odd elements ",
            str(odd_digits_count),
            "n the str",
            str(odd_digits_count),
            "ng ",
            str(odd_digits_count),
            " of the ",
            str(odd_digits_count),
            "nput."
        ]
        composed_message = ""
        for part in message_parts:
            composed_message += part
        results_collector.append(composed_message)
        current_index += 1

    return results_collector