def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = list(map(int, str(n)))
        digits[0] *= neg
        return sum(digits)

    sums_list = [digits_sum(i) for i in arr]
    filtered_list = [x for x in sums_list if x > 0]
    return len(filtered_list)