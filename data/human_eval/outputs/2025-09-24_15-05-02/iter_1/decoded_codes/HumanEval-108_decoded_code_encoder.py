def digs(x):
    return [int(d) for d in str(x)]

def count_nums(arr):
    def transformed_sum(n):
        digits = digs(abs(n))
        total = 0
        for i, d in enumerate(digits):
            sign = -1 if n < 0 and i == 0 else 1
            total += d * sign
        return total

    s_list = [transformed_sum(n) for n in arr]
    return sum(1 for s in s_list if s > 0)