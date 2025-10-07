class Solution:
    def clearStars(self, s: str) -> str:
        buffer = []
        for ch in s:
            if ch == "*":
                if buffer:
                    buffer.pop()
            else:
                buffer.append(ch)
        return "".join(buffer)