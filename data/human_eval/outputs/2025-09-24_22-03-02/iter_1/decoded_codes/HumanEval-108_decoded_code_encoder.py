def count_nums(arr):
    def digits_sum(n):
        neg = -1 if n < 0 else 1
        digits = [int(d) for d in str(abs(n))]
        digits[0] *= neg
        return sum(digits)
    return sum(1 for x in arr if digits_sum(x) > 0)