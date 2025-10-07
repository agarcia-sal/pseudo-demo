def intersperse(numbers: list[int], delimiter: int) -> list[int]:
    if not numbers:
        return []

    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])

    return result