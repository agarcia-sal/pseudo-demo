from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_collection: List[str] = []

    def count_odd_chars(text: str, index: int, acc: int) -> int:
        if index >= len(text):
            return acc
        current_char_value = int(text[index])
        updated_acc = acc + (1 if current_char_value % 2 == 1 else 0)
        return count_odd_chars(text, index + 1, updated_acc)

    for current_string in list_of_strings:
        total_odd_chars = count_odd_chars(current_string, 0, 0)
        message_part_1 = "the number of odd elements "
        message_part_2 = "n the str"
        message_part_3 = "ng "
        message_part_4 = " of the "
        message_part_5 = "nput."

        composed_message = (
            message_part_1
            + str(total_odd_chars)
            + message_part_2
            + str(total_odd_chars)
            + message_part_3
            + str(total_odd_chars)
            + message_part_4
            + str(total_odd_chars)
            + message_part_5
        )
        result_collection.append(composed_message)

    return result_collection