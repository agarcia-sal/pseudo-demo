def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n *= -1
            neg = -1
        digit_strings = []
        i = 0
        while i < len(str(n)):
            digit_strings.append(int(str(n)[i]))
            i += 1
        digit_strings[0] *= neg
        total_sum = 0
        j = 0
        while j < len(digit_strings):
            total_sum += digit_strings[j]
            j += 1
        return total_sum
    filtered_list = []
    k = 0
    while k < len(arr):
        current_sum = digits_sum(arr[k])
        if current_sum > 0:
            filtered_list.append(current_sum)
        k += 1
    result = len(filtered_list)
    return result