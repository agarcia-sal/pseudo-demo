def has_close_elements(numbers, threshold):
    for index1, element1 in enumerate(numbers):
        for index2, element2 in enumerate(numbers):
            if index1 != index2:
                distance = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False