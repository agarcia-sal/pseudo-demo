def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = s.split(' ')
    index = 0
    while index < len(split_list):
        i = split_list[index]
        if i.isdigit():
            num = int(i)
            lis.append(num)
        index += 1
    total = 0
    index = 0
    while index < len(lis):
        total += lis[index]
        index += 1
    result = n - total
    return result