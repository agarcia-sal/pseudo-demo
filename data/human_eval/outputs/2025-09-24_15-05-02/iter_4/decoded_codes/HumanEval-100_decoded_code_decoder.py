def make_a_pile(n):
    list_of_stones = []
    for i in range(n):
        stones_in_level = n + 2 * i
        list_of_stones.append(stones_in_level)
    return list_of_stones