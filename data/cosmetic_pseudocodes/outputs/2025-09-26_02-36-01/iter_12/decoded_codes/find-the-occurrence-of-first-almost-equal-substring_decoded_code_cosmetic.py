class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            n = len(substring)
            m = len(pattern)
            delta = 0

            def compare_chars(a: str, b: str) -> bool:
                return a != b

            pos = 0
            while pos < n and delta <= 1:
                if compare_chars(substring[pos], pattern[pos]):
                    delta += 1
                pos += 1
            return delta <= 1

        plen = len(pattern)
        result = -1

        def check_index(idx: int) -> bool:
            # Slice from idx to idx+plen (exclusive)
            return is_almost_equal(s[idx:idx + plen], pattern)

        current = 0
        found = False
        while True:
            if current + plen > len(s):
                found = False
                break
            if check_index(current):
                found = True
                break
            current += 1

        if found:
            result = current
        return result