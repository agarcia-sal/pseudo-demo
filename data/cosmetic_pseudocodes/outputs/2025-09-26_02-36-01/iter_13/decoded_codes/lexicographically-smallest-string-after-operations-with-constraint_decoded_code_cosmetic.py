class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            alt = 26 - diff
            return diff if diff < alt else alt

        length = len(s)
        # Convert string into 1-based index list of chars with a dummy at index 0
        chars = [''] + list(s)

        def process_position(position: int) -> None:
            nonlocal k
            if position >= length or k <= 0:
                return

            current_char = chars[position + 1]
            if current_char == 'a':
                process_position(position + 1)
                return

            distance = cyclic_distance(current_char, 'a')
            if distance <= k:
                chars[position + 1] = 'a'
                k -= distance
            else:
                new_char_code = ord(current_char) - k
                chars[position + 1] = chr(new_char_code)
                k = 0

            process_position(position + 1)

        process_position(0)

        output_string = ''
        pos = 1
        while True:
            if pos > length:
                break
            output_string += chars[pos]
            pos += 1

        return output_string