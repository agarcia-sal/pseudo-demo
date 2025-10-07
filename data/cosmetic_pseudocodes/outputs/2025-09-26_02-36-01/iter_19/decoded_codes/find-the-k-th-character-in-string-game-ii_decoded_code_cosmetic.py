class Solution:
    def kthCharacter(self, x: int, y: list[int]) -> str:
        n = 1
        strategy = []

        idx = 0
        while idx < len(y):
            elem = y[idx]
            strategy.append(elem)
            if elem == 0:
                n = n * 2
            else:
                n = 2 * n
            idx += 1

        letter = 'a'
        pos = len(strategy) - 1
        while pos >= 0:
            half = n // 2
            if x <= half:
                n = half
            else:
                x -= half
                n = half
                if strategy[pos] == 1:
                    s = ord(letter)
                    letter = 'a' if s == ord('z') else chr(s + 1)
            pos -= 1

        return letter