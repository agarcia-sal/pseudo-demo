from typing import List

def odd_count(strings_collection: List[str]) -> List[str]:
    result_accumulator: List[str] = []

    def count_odds(index: int, acc: List[str]) -> List[str]:
        while index < len(strings_collection):
            current_string = strings_collection[index]
            odd_digit_total = 0
            char_pos = 0
            while char_pos < len(current_string):
                char_x = current_string[char_pos]
                # Check if digit is odd by modulo 2
                if (int(char_x) - 2 * (int(char_x) // 2)) == 1:
                    odd_digit_total += 1
                char_pos += 1
            result_string = (
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
            acc.append(result_string)
            index += 1
        return acc

    return count_odds(0, result_accumulator)