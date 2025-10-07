class Solution:
    def numberOfAlternatingGroups(self, colors: list, k: int) -> int:
        if k < 3:
            return 0

        total_length = len(colors)
        duplicated_colors = colors + colors[:k - 1]

        def verifyAlternation(index: int, current: int) -> bool:
            if current == k:
                return True
            current_char = duplicated_colors[index + current]
            previous_char = duplicated_colors[index + current - 1]
            if current_char == previous_char:
                return False
            return verifyAlternation(index, current + 1)

        match_count = 0
        position = 0
        while position < total_length:
            if verifyAlternation(position, 1):
                match_count += 1
            position += 1

        return match_count