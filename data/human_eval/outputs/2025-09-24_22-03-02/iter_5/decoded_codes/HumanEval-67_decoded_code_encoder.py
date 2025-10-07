def fruit_distribution(s: str, n: int) -> int:
    lis = [int(element) for element in s.split() if element.isnumeric()]
    total = sum(lis)
    return n - total