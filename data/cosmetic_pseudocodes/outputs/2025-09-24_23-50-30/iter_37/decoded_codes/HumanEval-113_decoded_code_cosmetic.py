from typing import List


def odd_count(array_of_texts: List[str]) -> List[str]:
    result_collection: List[str] = []
    for text_entry in array_of_texts:
        count_tracker = sum((ord(symbol) % 2) == 1 for symbol in text_entry)
        message_piece = (
            "the number of odd elements "
            + str(count_tracker)
            + "n the str"
            + str(count_tracker)
            + "ng "
            + str(count_tracker)
            + " of the "
            + str(count_tracker)
            + "nput."
        )
        result_collection.append(message_piece)
    return result_collection