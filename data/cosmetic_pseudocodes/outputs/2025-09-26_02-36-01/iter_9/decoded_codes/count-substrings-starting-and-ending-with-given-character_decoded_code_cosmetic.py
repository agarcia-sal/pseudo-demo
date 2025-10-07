class Solution:
    def countSubstrings(self, t: str, u: str) -> int:
        def tallyOccurrences(v: str, x: str) -> int:
            a1 = 0
            for char in v:
                if char == x:
                    a1 += 1
            return a1

        d4 = tallyOccurrences(t, u)
        e5 = d4 * ((d4 + 1) // 2)  # Using integer division as count of substrings should be integral
        return e5