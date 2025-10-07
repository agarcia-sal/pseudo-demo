def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n = list(map(int, str(n)))
        n[0] = n[0] * neg
        return sum(n)

    sums_list = []
    for i in arr:
        sums_list.append(digits_sum(i))

    filtered_list = []
    for x in sums_list:
        if x > 0:
            filtered_list.append(x)

    return len(filtered_list)