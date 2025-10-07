from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def compute_relation(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        total_length = len(nums)
        pattern_length = len(pattern)
        tally = 0

        rels = []
        for i in range(total_length - 1):
            rels.append(compute_relation(nums[i], nums[i + 1]))

        # The pseudocode seems to compare subarrays of rels to pattern, with length pattern_length.
        # Since pattern_length is length of pattern (which is presumably a list of relations),
        # and rels has length total_length - 1, max starting pos is total_length - pattern_length - 1.
        # We use the provided bounds exactly.

        pos = 0
        while pos <= total_length - pattern_length - 1:
            segment = []
            offset = 0
            while offset <= pattern_length - 1:
                segment.append(rels[pos + offset])
                offset += 1

            if segment == pattern:
                tally += 1

            pos += 1

        return tally