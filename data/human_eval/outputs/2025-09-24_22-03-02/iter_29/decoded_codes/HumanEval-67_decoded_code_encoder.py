def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = s.split(' ')
    for i_index in range(len(split_list)):
        i = split_list[i_index]
        if i.isdigit():
            lis.append(int(i))
    total_sum = 0
    for sum_index in range(len(lis)):
        total_sum += lis[sum_index]
    return n - total_sum