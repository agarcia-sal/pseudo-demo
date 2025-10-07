from typing import List

def search(list_of_integers: List[int]) -> int:
    frequencyArr: List[int] = [0] * (max(list_of_integers, default=0) + 1)

    for num_element in list_of_integers:
        frequencyArr[num_element] += 1

    def check_frequency(pos: int) -> int:
        if pos > len(frequencyArr) - 1:
            return -1
        elif not (frequencyArr[pos] < pos):
            result = check_frequency(pos + 1)
            if result > pos:
                return result
            return pos
        return check_frequency(pos + 1)

    return check_frequency(1)