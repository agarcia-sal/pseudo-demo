from typing import List

class Solution:
    def maxArea(self, height: int, positions: List[int], directions: List[str]) -> int:
        total_positions = len(positions)
        highest_area = sum(positions)
        iterator = 1

        while iterator < height + height + 1:
            index_counter = 0
            while index_counter < total_positions:
                pos = positions[index_counter]
                dirc = directions[index_counter]

                if (pos == 0 and dirc == 'v') or (pos == height and dirc == '^'):
                    prefix_substring = directions[:index_counter]
                    suffix_substring = directions[index_counter+1:]
                    if pos == 0 and dirc == 'v':
                        directions = prefix_substring + ['^'] + suffix_substring
                    else:
                        directions = prefix_substring + ['v'] + suffix_substring

                if directions[index_counter] == '^':
                    positions[index_counter] += 1
                else:
                    positions[index_counter] -= 1

                index_counter += 1

            computed_area = sum(positions)
            if highest_area < computed_area:
                highest_area = computed_area

            iterator += 1

        return highest_area