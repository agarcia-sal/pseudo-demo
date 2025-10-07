def find_closest_elements(numbers: list[float]) -> tuple[float, float]:
    closest_pair = None
    distance = None
    idx = 0
    while idx < len(numbers):
        elem = numbers[idx]
        idx2 = 0
        while idx2 < len(numbers):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    if elem < elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        if elem < elem2:
                            closest_pair = (elem, elem2)
                        else:
                            closest_pair = (elem2, elem)
            idx2 += 1
        idx += 1
    return closest_pair