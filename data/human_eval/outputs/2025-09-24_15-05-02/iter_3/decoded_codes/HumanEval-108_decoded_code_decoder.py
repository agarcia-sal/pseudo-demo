def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = [int(d) for d in str(n)]
        digits[0] *= neg
        return sum(digits)

    sums = [digits_sum(i) for i in arr]
    filtered = [s for s in sums if s > 0]
    return len(filtered)