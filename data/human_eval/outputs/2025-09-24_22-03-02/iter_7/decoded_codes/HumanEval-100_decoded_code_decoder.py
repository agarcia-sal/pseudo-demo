def make_a_pile(n):
    stones_list = []
    for i in range(n):
        stones_count = n + 2 * i
        stones_list.append(stones_count)
    return stones_list