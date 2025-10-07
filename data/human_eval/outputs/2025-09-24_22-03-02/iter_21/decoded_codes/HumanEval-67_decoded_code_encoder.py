def fruit_distribution(s: str, n: int) -> int:
    lis = []
    words = s.split(' ')
    for i in words:
        if i.isdigit():
            number = int(i)
            lis.append(number)
    total = 0
    for value in lis:
        total += value
    result = n - total
    return result