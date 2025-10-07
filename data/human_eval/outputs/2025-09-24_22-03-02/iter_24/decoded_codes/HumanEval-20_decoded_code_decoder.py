from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    length_of_numbers = len(numbers)

    for idx in range(length_of_numbers):
        elem = numbers[idx]
        for idx2 in range(length_of_numbers):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    list_to_sort = []
                    list_to_sort.append(elem)
                    list_to_sort.append(elem2)
                    list_to_sort.sort()
                    closest_pair = (list_to_sort[0], list_to_sort[1])
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        list_to_sort = []
                        list_to_sort.append(elem)
                        list_to_sort.append(elem2)
                        list_to_sort.sort()
                        closest_pair = (list_to_sort[0], list_to_sort[1])

    return closest_pair