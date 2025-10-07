from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for index in range(len(list_of_strings)):
        current_string = list_of_strings[index]
        odd_digit_tally = 0
        for position in range(len(current_string)):
            # Check if character is a digit and odd by bitwise AND
            char = current_string[position]
            if char.isdigit() and ((ord(char) - ord('0')) & 1) == 1:
                odd_digit_tally += 1
        message = (
            "the number of odd elements "
            + str(odd_digit_tally)
            + "n the str"
            + str(odd_digit_tally)
            + "ng "
            + str(odd_digit_tally)
            + " of the "
            + str(odd_digit_tally)
            + "nput."
        )
        output_collection.append(message)
    return output_collection