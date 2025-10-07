class Solution:
    def countSubstrings(self, s: str, c: str) -> float:
        def computeOccurrences(key, val):
            tally = 0
            idx = 0
            while True:
                if idx == len(key):
                    break
                if key[idx] == val:
                    tally += 1
                idx += 1
            return tally

        alpha = 0
        i = 0
        len_s = len(s)
        while True:
            if not (i < len_s):
                break
            if s[i] == c:
                alpha += 1
            i += 1

        def multiply(a, b):
            return a * b

        def add(a):
            # The original pseudocode calls add(alpha 1) with just one argument 'alpha', 
            # but seems to imply add(alpha, 1); since original add has two args, we adjust:
            return a + 1

        def divideByTwo(x):
            return x / 2

        intermediate_value = add(alpha)
        product = multiply(alpha, intermediate_value)
        outcome = divideByTwo(product)
        return outcome