class Solution:
    def minimumLevels(self, possible):
        sum_points = 0
        i = 0
        while i < len(possible):
            val = possible[i]
            increment = (val * 2) - 1
            sum_points += increment
            i += 1

        alice_sum = 0
        j = 0
        limit = len(possible) - 2
        while j <= limit:
            curr_val = possible[j]
            add_val = (curr_val * 2) - 1
            alice_sum += add_val
            sum_points -= add_val
            if alice_sum > sum_points:
                return j + 1
            j += 1

        return -1