class Solution:
    def clearStars(self, s: str) -> str:
        container = []
        index = 0
        while index < len(s):
            current_character = s[index]
            if current_character == "*":
                if len(container) > 0:
                    container.pop()
            else:
                container.append(current_character)
            index += 1
        combined_string = ""
        iterator = 0
        while iterator < len(container):
            combined_string += container[iterator]
            iterator += 1
        return combined_string