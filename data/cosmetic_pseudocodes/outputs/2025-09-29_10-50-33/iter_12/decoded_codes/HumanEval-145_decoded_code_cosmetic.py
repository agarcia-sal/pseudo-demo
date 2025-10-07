from typing import List

def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        sign_state: int = 1
        if number < 0:
            number = -number
            sign_state = -1
        digits_collection: List[int] = [int(ch) for ch in str(number)]
        digits_collection[0] *= sign_state
        return sum(digits_collection)
    return sorted(list_of_numbers, key=digits_sum)