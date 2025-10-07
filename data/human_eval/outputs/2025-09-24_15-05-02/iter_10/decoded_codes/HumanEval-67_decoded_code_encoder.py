def fruit_distribution(s, n):
    lis = []
    for i in s.split():
        if i.isdigit():
            lis.append(int(i))
    total_apples_and_oranges = 0
    for number in lis:
        total_apples_and_oranges += number
    mangoes = n - total_apples_and_oranges
    return mangoes