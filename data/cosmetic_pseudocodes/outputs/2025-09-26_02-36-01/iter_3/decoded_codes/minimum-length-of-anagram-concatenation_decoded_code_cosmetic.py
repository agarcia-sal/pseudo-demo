class Solution:
    def minAnagramLength(self, s):
        distinctElements = set()
        iterator = 0
        while iterator < len(s):
            distinctElements.add(s[iterator])
            iterator += 1
        return len(distinctElements)