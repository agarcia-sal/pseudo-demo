class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        bag = {}
        cache = {}
        pos = 0
        while pos < len(word):
            ch = word[pos]
            if ch not in bag:
                bag[ch] = pos
            cache[ch] = pos
            pos += 1

        def helperAlpha():
            lowerSet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
            upperSet = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
            return zip(lowerSet, upperSet)

        acc = 0
        for x, y in helperAlpha():
            if x in cache and y in bag and cache[x] < bag[y]:
                acc += 1

        return acc