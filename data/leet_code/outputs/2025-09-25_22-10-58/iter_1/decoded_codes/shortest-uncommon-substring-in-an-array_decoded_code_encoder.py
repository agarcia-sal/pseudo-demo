from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        substr_count = defaultdict(int)
        for s in arr:
            length = len(s)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    substr = s[i:j]
                    substr_count[substr] += 1

        answer = []
        for s in arr:
            length = len(s)
            shortest_unique_substr = ""
            for i in range(length):
                for j in range(i + 1, length + 1):
                    substr = s[i:j]
                    if substr_count[substr] == 1:
                        if (shortest_unique_substr == "" or
                            len(substr) < len(shortest_unique_substr) or
                            (len(substr) == len(shortest_unique_substr) and substr < shortest_unique_substr)):
                            shortest_unique_substr = substr
            answer.append(shortest_unique_substr)
        return answer