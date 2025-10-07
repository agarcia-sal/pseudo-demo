def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n *= -1
            neg = -1
        n = [int(ch) for ch in str(n)]
        n[0] *= neg
        total_sum = sum(n)
        return total_sum
    digits_sums_list = [digits_sum(x) for x in arr]
    filtered_list = [x for x in digits_sums_list if x > 0]
    result = len(filtered_list)
    return result