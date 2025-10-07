class Solution:
    def clearStars(self, s: str) -> str:
        accumulator = []
        index = 0
        while index < len(s):
            current_char = s[index]
            if current_char == '*':
                if accumulator:
                    accumulator.pop()
            else:
                accumulator.append(current_char)
            index += 1
        output = ""
        pos = 0
        while pos < len(accumulator):
            output += accumulator[pos]
            pos += 1
        return output