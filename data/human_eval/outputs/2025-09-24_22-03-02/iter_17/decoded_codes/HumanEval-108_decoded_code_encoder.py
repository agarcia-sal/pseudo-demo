def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n_list = [int(i) for i in str(n)]
        n_list[0] *= neg
        total_sum = sum(n_list)
        return total_sum
    digit_sums = [digits_sum(i) for i in arr]
    filtered_list = [x for x in digit_sums if x > 0]
    result = len(filtered_list)
    return result