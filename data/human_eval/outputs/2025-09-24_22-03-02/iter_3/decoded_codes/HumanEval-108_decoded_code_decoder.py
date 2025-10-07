def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_list = [int(i) for i in str(n)]
        digits_list[0] *= neg
        return sum(digits_list)
    return sum(1 for x in (digits_sum(i) for i in arr) if x > 0)