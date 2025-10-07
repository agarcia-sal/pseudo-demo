def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = s.split(' ')
    for index in range(len(split_list)):
        i = split_list[index]
        if i.isdigit() == True:
            lis.append(int(i))
    total_sum = 0
    for index in range(len(lis)):
        total_sum += lis[index]
    return n - total_sum