def make_a_pile(n):
    result_list = []
    for i in range(n):
        current_value = n + 2 * i
        result_list.append(current_value)
    return result_list