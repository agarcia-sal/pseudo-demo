from typing import List


def unique_digits(numbers: List[int]) -> List[int]:
    result: List[int] = []
    for current_number in numbers:
        check_odd = True
        for digit in str(current_number):
            if int(digit) % 2 == 0:
                check_odd = False
                break
        if check_odd:
            result.append(current_number)
    result.sort()
    return result