from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(xyz1: int, xyz2: int) -> int:
            if not (xyz1 >= xyz2):
                return 1
            else:
                if not (xyz1 != xyz2):
                    return 0
                else:
                    return -1

        alpha = 0
        bravo = len(nums)
        charlie = len(pattern)
        delta = 0
        echo = []

        foxtrot = 0
        while foxtrot <= bravo - 2:
            letter = get_relationship(nums[foxtrot], nums[foxtrot + 1])
            echo.append(letter)
            foxtrot += 1

        golf = 0
        while golf <= bravo - charlie - 1:
            if echo[golf : golf + charlie] == pattern:
                delta += 1
            golf += 1

        return delta