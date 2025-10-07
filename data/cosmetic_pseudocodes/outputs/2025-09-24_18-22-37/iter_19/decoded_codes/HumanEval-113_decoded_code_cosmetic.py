from typing import List

def odd_count(collection_of_texts: List[str]) -> List[str]:
    aggregated_results: List[str] = []
    idx1: int = 0
    while idx1 < len(collection_of_texts):
        current_text: str = collection_of_texts[idx1]
        odd_digit_counter: int = 0
        idx2: int = 0
        while True:
            if idx2 >= len(current_text):
                break
            character_to_check: str = current_text[idx2]
            numeric_val: int = int(character_to_check)
            if numeric_val % 2 == 1:
                odd_digit_counter += 1
            idx2 += 1
        concatenated_title: str = (
            "the number of odd elements "
            + str(odd_digit_counter)
            + "n the str"
            + str(odd_digit_counter)
            + "ng "
            + str(odd_digit_counter)
            + " of the "
            + str(odd_digit_counter)
            + "nput."
        )
        aggregated_results.append(concatenated_title)
        idx1 += 1
    return aggregated_results