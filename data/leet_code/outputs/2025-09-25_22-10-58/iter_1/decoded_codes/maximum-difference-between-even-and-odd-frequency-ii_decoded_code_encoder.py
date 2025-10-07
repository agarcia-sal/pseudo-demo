from collections import defaultdict
from math import inf
from itertools import product

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = float('-inf')
        chars = "zeroone two three four".replace(" ", "")
        # Given chars in pseudocode: "zero one two three four"
        # The distinct characters for permutations come from "zero one two three four"
        # but those words are concatenated. The original pseudocode suggests:
        # permutations of pairs (a, b) such that a is from "zero one two three four"
        # So the characters are: 'z','e','r','o',' ','o','n','e',' ',... but spaces
        # So presumably this means characters: 'z','e','r','o','n','t','w','h','f','u','r'?
        # But to exactly match pseudocode "zero one two three four" as string, one can parse as:
        # letters of "zero one two three four" without space
        # Which means chars = "zeroonetwothreefour"
        # Distinct characters: z,e,r,o,n,t,w,h,f,u
        # The pseudocode is ambiguous, but the simplest is to take the string "zeroonetwothreefour" and get unique chars.
        chars = "zeroonetwothreefour"
        unique_chars = sorted(set(chars))
        ans = float('-inf')

        # All pairs (a,b) with distinct a,b from unique_chars
        for a, b in product(unique_chars, repeat=2):
            if a == b:
                continue

            minDiff = defaultdict(lambda: inf)
            prefixA = [0]
            prefixB = [0]
            l = 0
            for r, c in enumerate(s):
                prefixA.append(prefixA[-1] + (1 if c == a else 0))
                prefixB.append(prefixB[-1] + (1 if c == b else 0))

                while (r - l + 1) >= k and prefixA[l] < prefixA[-1] and prefixB[l] < prefixB[-1]:
                    paritiesKey = (prefixA[l] % 2, prefixB[l] % 2)
                    current = prefixA[l] - prefixB[l]
                    if current < minDiff[paritiesKey]:
                        minDiff[paritiesKey] = current
                    l += 1

                parity_key = ((1 - (prefixA[-1] % 2)), (prefixB[-1] % 2))
                candidate = prefixA[-1] - prefixB[-1] - minDiff[parity_key]
                if candidate > ans:
                    ans = candidate

        return ans