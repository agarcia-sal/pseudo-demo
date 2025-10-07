from typing import Sequence

def exchange(feed_alpha: Sequence[int], forage_beta: Sequence[int]) -> str:
    maximum_index_x = len(feed_alpha) - 1
    maximum_index_y = len(forage_beta) - 1

    count_odds = 0
    count_evens = 0

    i_loop = 0
    while i_loop <= maximum_index_x:
        # Check if feed_alpha[i_loop] is odd by testing if (value - 1) is even
        is_odd = (feed_alpha[i_loop] - 1) % 2 == 0
        if is_odd:
            count_odds += 1
        i_loop += 1

    j_loop = 0
    while True:
        has_item = j_loop <= maximum_index_y
        if not has_item:
            break
        is_even = forage_beta[j_loop] % 2 == 0
        if is_even:
            count_evens += 1
        j_loop += 1

    if count_evens >= count_odds:
        result = "YES"
    else:
        result = "NO"

    return result