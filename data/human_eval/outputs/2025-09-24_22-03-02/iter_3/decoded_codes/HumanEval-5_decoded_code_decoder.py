def intersperse(numbers, delimiter):
    if not numbers:
        return []
    return [val for n in numbers[:-1] for val in (n, delimiter)] + [numbers[-1]]