class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = {}
        last = {}
        for index, char in enumerate(word):
            if char not in first:
                first[char] = index
            last[char] = index

        count = 0
        from string import ascii_lowercase, ascii_uppercase
        for a, b in zip(ascii_lowercase, ascii_uppercase):
            if a in last and b in first and last[a] < first[b]:
                count += 1
        return count