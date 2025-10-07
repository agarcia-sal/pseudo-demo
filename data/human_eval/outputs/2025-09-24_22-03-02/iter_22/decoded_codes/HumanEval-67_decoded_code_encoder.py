def fruit_distribution(s: str, n: int) -> int:
    lis = []
    parts = s.split(" ")
    for index in range(len(parts)):
        i = parts[index]
        if i.isdigit():
            lis.append(int(i))
    total = 0
    for index in range(len(lis)):
        total += lis[index]
    return n - total