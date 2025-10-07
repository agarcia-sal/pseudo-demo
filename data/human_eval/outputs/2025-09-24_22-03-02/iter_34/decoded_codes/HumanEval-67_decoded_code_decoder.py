def fruit_distribution(s: str, n: int) -> int:
    lis = []
    words = s.split(" ")
    for idx in range(len(words)):
        i = words[idx]
        if i.isdigit():
            number = int(i)
            lis.append(number)
    total = 0
    for idx in range(len(lis)):
        total += lis[idx]
    result = n - total
    return result