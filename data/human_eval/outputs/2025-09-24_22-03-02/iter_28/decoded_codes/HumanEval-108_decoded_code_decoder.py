def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        digit_list = []
        str_n = str(n)
        index = 0
        while index < len(str_n):
            digit_list.append(int(str_n[index]))
            index += 1
        digit_list[0] = digit_list[0] * neg
        sum_digits = 0
        idx = 0
        while idx < len(digit_list):
            sum_digits += digit_list[idx]
            idx += 1
        return sum_digits

    filtered_list = []
    i = 0
    while i < len(arr):
        digit_sum_value = digits_sum(arr[i])
        if digit_sum_value > 0:
            filtered_list.append(arr[i])
        i += 1
    count = len(filtered_list)
    return count