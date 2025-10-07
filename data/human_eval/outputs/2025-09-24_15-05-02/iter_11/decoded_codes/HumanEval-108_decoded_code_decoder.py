def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = [int(d) for d in str(n)]
        digits[0] *= neg
        return sum(digits)

    digit_sums = []
    for element in arr:
        digit_sums.append(digits_sum(element))

    filtered_list = [x for x in digit_sums if x > 0]

    return len(filtered_list)