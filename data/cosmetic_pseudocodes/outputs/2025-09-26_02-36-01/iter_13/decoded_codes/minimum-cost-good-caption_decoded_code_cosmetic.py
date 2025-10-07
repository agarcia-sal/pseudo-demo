class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        total_length = len(caption)
        if total_length < 3:
            return ""

        char_list = [caption[i] for i in range(total_length)]

        def expandLeftRight(idx_left, idx_right, arr):
            new_left = idx_left
            new_right = idx_right
            while new_left > 0 and arr[new_left - 1] == arr[new_left]:
                new_left -= 1
            while new_right < len(arr) - 1 and arr[new_right + 1] == arr[new_right]:
                new_right += 1
            return new_left, new_right

        def nextAlphabetChar(ch):
            if ch == "a":
                return "b"
            elif ch == "z":
                return "y"
            else:
                return chr(ord(ch) + 1)

        def fillRange(arr, start_idx, length_fill, fill_char):
            fill_end = start_idx + length_fill
            pos = start_idx
            while pos < fill_end:
                arr[pos] = fill_char
                pos += 1

        position = 0
        limit = total_length

        while position < limit:
            segment_start = position
            while position < limit and char_list[position] == char_list[segment_start]:
                position += 1

            segment_len = position - segment_start

            if segment_len < 3:
                left_extend = False
                right_extend = False

                if segment_start > 0 and char_list[segment_start - 1] == char_list[segment_start]:
                    char_list[segment_start - 1] = char_list[segment_start]
                    segment_start -= 1
                    segment_len += 1
                    left_extend = True

                if position < limit and char_list[position - 1] == char_list[position]:
                    char_list[position] = char_list[position - 1]
                    position += 1
                    segment_len += 1
                    right_extend = True

                if segment_len < 3:
                    if segment_start > 0:
                        focus_char = char_list[segment_start - 1]
                    else:
                        focus_char = char_list[position] if position < limit else char_list[segment_start]

                    if focus_char == "a":
                        replacement_char = "b"
                    elif focus_char == "z":
                        replacement_char = "y"
                    else:
                        replacement_char = nextAlphabetChar(focus_char)

                    fillRange(char_list, segment_start, segment_len, replacement_char)

                    position = segment_start + segment_len

        result_string = ""
        cursor = 0
        while cursor < len(char_list):
            result_string += char_list[cursor]
            cursor += 1

        return result_string