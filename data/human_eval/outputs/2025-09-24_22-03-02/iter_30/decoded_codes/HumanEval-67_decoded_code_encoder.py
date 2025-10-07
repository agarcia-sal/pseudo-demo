def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = s.split(' ')
    for i in split_list:
        if i.isdigit():
            number = int(i)
            lis.append(number)
    total_sum = 0
    for num in lis:
        total_sum += num
    result = n - total_sum
    return result