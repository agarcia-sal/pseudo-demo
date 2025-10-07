def count_nums(arr):
    def digits_sum(n) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        n_str = str(n)
        n_list = []
        for i in range(len(n_str)):
            n_list.append(int(n_str[i]))
        n_list[0] = n_list[0] * neg
        total_sum = 0
        for index in range(len(n_list)):
            total_sum += n_list[index]
        return total_sum

    digit_sums = []
    for index in range(len(arr)):
        current_value = digits_sum(arr[index])
        digit_sums.append(current_value)
    filtered_list = []
    for index in range(len(digit_sums)):
        if digit_sums[index] > 0:
            filtered_list.append(digit_sums[index])
    result = len(filtered_list)
    return result