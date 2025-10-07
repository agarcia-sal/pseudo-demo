def find_closest_elements(numbers):
    numbers = sorted(numbers)
    closest_pair = None
    distance = None

    for i in range(len(numbers) - 1):
        new_distance = abs(numbers[i] - numbers[i + 1])
        if distance is None or new_distance < distance:
            distance = new_distance
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair