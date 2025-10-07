def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        digits_list = []
        n_string = str(n)
        for index in range(len(n_string)):
            digit_char = n_string[index]
            digit_int = int(digit_char)
            digits_list.append(digit_int)
        digits_list[0] = digits_list[0] * neg
        total_sum = 0
        for index in range(len(digits_list)):
            total_sum += digits_list[index]
        return total_sum

    sums_list = []
    for index in range(len(arr)):
        current_element = arr[index]
        current_sum = digits_sum(current_element)
        sums_list.append(current_sum)

    filtered_list = []
    for index in range(len(sums_list)):
        if sums_list[index] > 0:
            filtered_list.append(sums_list[index])

    return len(filtered_list)