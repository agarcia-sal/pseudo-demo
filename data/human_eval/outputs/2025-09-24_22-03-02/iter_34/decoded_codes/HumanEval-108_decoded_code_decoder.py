def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_string = str(n)
        n = []
        i = 0
        while i < len(digits_string):
            digit_char = digits_string[i]
            digit_int = int(digit_char)
            n.append(digit_int)
            i += 1
        n[0] = n[0] * neg
        total_sum = 0
        j = 0
        while j < len(n):
            total_sum += n[j]
            j += 1
        return total_sum

    digit_sums = []
    k = 0
    while k < len(arr):
        element = arr[k]
        sum_value = digits_sum(element)
        digit_sums.append(sum_value)
        k += 1

    positive_sums = []
    m = 0
    while m < len(digit_sums):
        if digit_sums[m] > 0:
            positive_sums.append(digit_sums[m])
        m += 1

    result = len(positive_sums)
    return result