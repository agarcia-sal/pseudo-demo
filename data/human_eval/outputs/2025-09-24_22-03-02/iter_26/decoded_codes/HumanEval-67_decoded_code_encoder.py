def fruit_distribution(s, n):
    lis = []
    split_list = s.split(' ')
    for i in split_list:
        if i.isdigit():
            lis.append(int(i))
    total_sum = sum(lis)
    result = n - total_sum
    return result