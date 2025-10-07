def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        n_str = str(n)
        digits = []
        for i in range(len(n_str)):
            digit_char = n_str[i]
            digit_int = int(digit_char)
            digits.append(digit_int)
        digits[0] = digits[0] * neg
        total_sum = 0
        for i in range(len(digits)):
            total_sum += digits[i]
        return total_sum
    sums_list = []
    for i in range(len(arr)):
        current_element = arr[i]
        current_sum = digits_sum(current_element)
        sums_list.append(current_sum)
    count = 0
    for i in range(len(sums_list)):
        if sums_list[i] > 0:
            count += 1
    return count