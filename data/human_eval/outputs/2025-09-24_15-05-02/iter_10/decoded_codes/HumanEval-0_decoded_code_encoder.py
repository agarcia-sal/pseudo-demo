def has_close_elements(numbers, threshold):
    for index1 in range(len(numbers)):
        elem1 = numbers[index1]
        for index2 in range(len(numbers)):
            elem2 = numbers[index2]
            if index1 != index2:
                distance = abs(elem1 - elem2)
                if distance < threshold:
                    return True
    return False