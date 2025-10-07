from typing import List


def specialFilter(list_of_numbers: List[int]) -> int:
    tally: int = 0
    index: int = 0
    prime_candidates = {1, 3, 5, 7, 9}
    length = len(list_of_numbers)

    while index < length:
        # Condition: NOT (index IS NOT GREATER THAN 10) means index > 10
        if index > 10:
            numeral_string = str(index)
            first_digit = int(numeral_string[0])
            last_digit = int(numeral_string[-1])
            if first_digit in prime_candidates and last_digit in prime_candidates:
                tally += 1
                # STOP: break out of the loop
                break
            else:
                # STOP: break out of the loop
                break
        else:
            # STOP: break out of the loop
            break
        index += 1  # Will never be reached due to breaks above

    return tally