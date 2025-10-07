def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_string = str(n)
        n = [int(c) for c in digits_string]
        n[0] *= neg
        total_sum = sum(n)
        return total_sum

    sums_list = [digits_sum(i) for i in arr]
    filtered_list = [x for x in sums_list if x > 0]
    result = len(filtered_list)
    return result