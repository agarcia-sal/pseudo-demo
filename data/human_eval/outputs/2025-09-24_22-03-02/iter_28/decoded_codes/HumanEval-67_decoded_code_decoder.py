def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = []
    index = 0
    while index < len(s):
        start = index
        while index < len(s) and s[index] != ' ':
            index += 1
        word = s[start:index]
        split_list.append(word)
        index += 1
    i_index = 0
    while i_index < len(split_list):
        i = split_list[i_index]
        if i.isdigit():
            lis.append(int(i))
        i_index += 1
    total_sum = 0
    sum_index = 0
    while sum_index < len(lis):
        total_sum += lis[sum_index]
        sum_index += 1
    return n - total_sum