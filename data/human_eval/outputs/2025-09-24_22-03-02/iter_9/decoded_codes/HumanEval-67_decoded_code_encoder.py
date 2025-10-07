def fruit_distribution(s: str, n: int) -> int:
    lis = [int(i) for i in s.split() if i.isdigit()]
    return n - sum(lis)