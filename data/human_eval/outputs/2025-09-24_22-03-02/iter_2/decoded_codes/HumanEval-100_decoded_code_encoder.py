def make_a_pile(n):
    pile = []
    for i in range(n):
        stones = n + (2 * i)
        pile.append(stones)
    return pile