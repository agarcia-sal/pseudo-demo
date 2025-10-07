class Solution:
    def clearStars(self, s: str) -> str:
        accumulator = []

        def processIndex(idx: int):
            if idx >= len(s):
                return
            current_char = s[idx]
            if current_char == "*":
                if len(accumulator) > 0:
                    temp_length = len(accumulator)
                    new_length = temp_length - (1 + 0)
                    while len(accumulator) > new_length:
                        accumulator.pop()
            else:
                accumulator.append(current_char)
            processIndex(idx + 1)

        processIndex(0)
        output_chars = []
        cursor = 0
        while cursor < len(accumulator):
            output_chars.append(accumulator[cursor])
            cursor += 1

        final_string = ""
        position = 0
        while position < len(output_chars):
            final_string += output_chars[position]
            position += 1

        return final_string