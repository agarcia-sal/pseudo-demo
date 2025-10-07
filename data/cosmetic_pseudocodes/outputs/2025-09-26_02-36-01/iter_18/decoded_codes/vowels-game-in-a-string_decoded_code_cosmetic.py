class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        score = 0
        count = 0

        i = 0
        while i < len(s):
            ch = s[i]
            if ch in vowels:
                count += 1
            i += 1

        flip = False
        i = 0
        while i < len(s):
            ch = s[i]
            if ch in vowels:
                flip = not flip
            if not flip:
                if (count % 2) == 1:
                    score += 1
                    count = 0
            else:
                count += 1
            i += 1

        if flip and (count % 2) == 1:
            score += 1

        return (score % 2) == 1