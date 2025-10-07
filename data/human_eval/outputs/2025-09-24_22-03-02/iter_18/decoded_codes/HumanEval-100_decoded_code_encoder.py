def make_a_pile(n):
    pile = []
    i = 0
    while i < n:
        current_stones = n + 2 * i
        pile.append(current_stones)
        i += 1
    return pile