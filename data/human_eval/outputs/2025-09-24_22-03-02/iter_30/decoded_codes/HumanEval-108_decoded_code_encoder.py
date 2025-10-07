def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n *= -1
            neg = -1
        digits_string = str(n)
        digits_list = []
        for index in range(len(digits_string)):
            digits_list.append(int(digits_string[index]))
        digits_list[0] *= neg
        total_sum = 0
        for index in range(len(digits_list)):
            total_sum += digits_list[index]
        return total_sum

    sums_list = []
    for index in range(len(arr)):
        current_sum = digits_sum(arr[index])
        sums_list.append(current_sum)

    filtered_list = []
    for index in range(len(sums_list)):
        if sums_list[index] > 0:
            filtered_list.append(sums_list[index])

    result = len(filtered_list)
    return result