def has_close_elements(numbers: list[float], threshold: float) -> bool:
    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            if idx != idx2:
                elem2 = numbers[idx2]
                difference = elem - elem2
                distance = -difference if difference < 0 else difference
                if distance < threshold:
                    return True
    return False