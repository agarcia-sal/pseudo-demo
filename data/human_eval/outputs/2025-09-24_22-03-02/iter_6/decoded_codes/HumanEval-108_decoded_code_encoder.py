def count_nums(arr):
    def digits_sum(number):
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digits = list(map(int, str(number)))
        digits[0] *= sign
        return sum(digits)
    digit_sums = [digits_sum(e) for e in arr]
    positive_sums = [x for x in digit_sums if x > 0]
    return len(positive_sums)