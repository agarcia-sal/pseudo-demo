def fruit_distribution(s: str, n: int) -> int:
    lis = [int(element) for element in s.split() if element.isdigit()]
    return n - sum(lis)