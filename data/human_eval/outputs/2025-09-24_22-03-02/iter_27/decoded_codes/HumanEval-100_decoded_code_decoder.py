def make_a_pile(n):
    stones_list = []
    index = 0
    while index < n:
        current_stones = n + 2 * index
        stones_list.append(current_stones)
        index += 1
    return stones_list