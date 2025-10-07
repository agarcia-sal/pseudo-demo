def make_a_pile(n):
    result_list = []
    for i in range(n):
        stone_count = n + 2 * i
        result_list.append(stone_count)
    return result_list