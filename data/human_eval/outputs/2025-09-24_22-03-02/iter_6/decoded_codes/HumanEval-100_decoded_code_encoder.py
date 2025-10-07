def make_a_pile(n):
    stones_list = []
    for index in range(n):
        stones_in_level = n + 2 * index
        stones_list.append(stones_in_level)
    return stones_list