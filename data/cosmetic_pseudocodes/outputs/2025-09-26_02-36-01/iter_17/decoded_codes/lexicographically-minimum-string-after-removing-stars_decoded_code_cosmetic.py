class Solution:
    def clearStars(self, s: str) -> str:
        result = []
        for ch in s:
            if ch != '*':
                result.append(ch)
            else:
                if result:
                    result.pop()
        return ''.join(result)