def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        n_str = str(n)
        n = []
        i = 0
        while i < len(n_str):
            n.append(int(n_str[i]))
            i += 1
        n[0] = n[0] * neg
        total_sum = 0
        j = 0
        while j < len(n):
            total_sum += n[j]
            j += 1
        return total_sum
    filtered_list = []
    k = 0
    while k < len(arr):
        current_value = digits_sum(arr[k])
        if current_value > 0:
            filtered_list.append(current_value)
        k += 1
    result = len(filtered_list)
    return result