def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits_list = []
        string_n = str(n)
        for char in string_n:
            digits_list.append(int(char))
        digits_list[0] *= neg
        total_sum = sum(digits_list)
        return total_sum

    filtered_list = []
    for i in arr:
        if digits_sum(i) > 0:
            filtered_list.append(i)
    return len(filtered_list)