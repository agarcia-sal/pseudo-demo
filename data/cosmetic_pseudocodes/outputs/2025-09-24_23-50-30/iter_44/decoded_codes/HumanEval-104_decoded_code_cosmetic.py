from typing import Iterable, List

def unique_digits(input_sequence: Iterable[int]) -> List[int]:
    def check_all_odd(num: int, place: int) -> bool:
        if place < 1:
            return True
        if ((num // place) % 10) % 2 == 0:
            return False
        return check_all_odd(num, place // 10)

    result_container: List[int] = []
    for element in input_sequence:
        max_place = 1
        while max_place <= element:
            max_place *= 10
        max_place //= 10
        if check_all_odd(element, max_place):
            result_container.append(element)

    return sorted(result_container)