class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        total_points = sum(2 * num - 1 for num in possible)
        alice_points = 0
        for index in range(len(possible) - 1):
            alice_points += 2 * possible[index] - 1
            total_points -= 2 * possible[index] - 1
            if alice_points > total_points:
                return index + 1
        return -1