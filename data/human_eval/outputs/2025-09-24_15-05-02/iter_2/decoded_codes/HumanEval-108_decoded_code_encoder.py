def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_list = [int(d) for d in str(n)]
        digits_list[0] *= neg
        return sum(digits_list)

    digit_sums = []
    for i in arr:
        digit_sums.append(digits_sum(i))

    positive_sums = [x for x in digit_sums if x > 0]
    return len(positive_sums)