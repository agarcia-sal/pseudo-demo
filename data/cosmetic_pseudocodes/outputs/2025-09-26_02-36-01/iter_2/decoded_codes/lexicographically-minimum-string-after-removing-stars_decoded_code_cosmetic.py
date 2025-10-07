class Solution:
    def clearStars(self, input_string: str) -> str:
        container = []
        idx = 0
        while idx < len(input_string):
            current_char = input_string[idx]
            if current_char == "*":
                if container:
                    container.pop()
            else:
                container.append(current_char)
            idx += 1
        output_string = ''.join(container)
        return output_string