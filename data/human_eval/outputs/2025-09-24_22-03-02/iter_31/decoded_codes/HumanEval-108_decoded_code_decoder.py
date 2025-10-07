def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n_str = str(n)
        n_list = []
        for char in n_str:
            digit = int(char)
            n_list.append(digit)
        n_list[0] *= neg
        total_sum = sum(n_list)
        return total_sum

    sums_list = [digits_sum(x) for x in arr]
    filtered_list = [x for x in sums_list if x > 0]
    return len(filtered_list)