from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for i in range(len(list_of_strings)):
        current_text = list_of_strings[i]
        odd_digits_counter = 0
        for j in range(len(current_text)):
            digit_value = int(current_text[j])
            if digit_value % 2 == 1:
                odd_digits_counter += 1
        phrase = (
            "the number of odd elements "
            + str(odd_digits_counter)
            + "n the str"
            + str(odd_digits_counter)
            + "ng "
            + str(odd_digits_counter)
            + " of the "
            + str(odd_digits_counter)
            + "nput."
        )
        output_collection.append(phrase)
    return output_collection