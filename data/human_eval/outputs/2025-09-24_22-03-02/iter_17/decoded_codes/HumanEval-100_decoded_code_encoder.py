def make_a_pile(n):
    stones_list = []
    for i in range(n):
        current_stones = n + 2 * i
        stones_list.append(current_stones)
    return stones_list