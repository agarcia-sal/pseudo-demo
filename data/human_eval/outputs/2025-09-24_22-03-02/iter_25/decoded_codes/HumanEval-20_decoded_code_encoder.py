from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None
    length = len(numbers)
    for i in range(length):
        elem = numbers[i]
        for j in range(length):
            if i != j:
                elem2 = numbers[j]
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    pair_list = [elem, elem2]
                    if pair_list[0] > pair_list[1]:
                        pair_list[0], pair_list[1] = pair_list[1], pair_list[0]
                    closest_pair = (pair_list[0], pair_list[1])
    return closest_pair