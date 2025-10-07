def fruit_distribution(s: str, n: int) -> int:
    numbers = []
    for item in s.split():
        if item.isdigit():
            numbers.append(int(item))
    return n - sum(numbers)