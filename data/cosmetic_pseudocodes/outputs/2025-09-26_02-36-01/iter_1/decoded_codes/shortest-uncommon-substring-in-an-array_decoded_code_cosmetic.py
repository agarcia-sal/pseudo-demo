from collections import defaultdict
from typing import List, Optional

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[Optional[str]]:
        frequency_map = defaultdict(int)

        for word in arr:
            n = len(word)
            for start_pos in range(n):
                for end_pos in range(start_pos + 1, n + 1):
                    fragment = word[start_pos:end_pos]
                    frequency_map[fragment] += 1

        results = []

        for word in arr:
            n = len(word)
            candidate: Optional[str] = None

            for start_pos in range(n):
                for end_pos in range(start_pos + 1, n + 1):
                    fragment = word[start_pos:end_pos]
                    if frequency_map[fragment] == 1:
                        if (candidate is None or 
                            len(fragment) < len(candidate) or 
                            (len(fragment) == len(candidate) and fragment < candidate)):
                            candidate = fragment

            results.append(candidate)

        return results