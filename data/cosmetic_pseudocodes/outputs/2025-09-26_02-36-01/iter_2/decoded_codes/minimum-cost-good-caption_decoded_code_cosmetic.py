class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        length_caption = len(caption)
        if length_caption < 3:
            return ""

        chars_list = list(caption)
        idx = 0

        while idx < length_caption:
            segment_start = idx
            # find segment of consecutive identical chars
            while idx < length_caption and chars_list[idx] == chars_list[segment_start]:
                idx += 1

            segment_length = idx - segment_start
            if segment_length < 3:
                # try to extend segment backward
                if segment_start > 0 and chars_list[segment_start - 1] == chars_list[segment_start]:
                    chars_list[segment_start - 1] = chars_list[segment_start]
                    segment_start -= 1
                    segment_length += 1
                # try to extend segment forward
                if idx < length_caption and chars_list[idx - 1] == chars_list[idx]:
                    chars_list[idx] = chars_list[idx - 1]
                    idx += 1
                    segment_length += 1
                # if still less than 3, replace all in segment with replacement_char
                if segment_length < 3:
                    if segment_start > 0:
                        adjacent_char = chars_list[segment_start - 1]
                    else:
                        adjacent_char = chars_list[idx]
                    if adjacent_char == 'a':
                        replacement_char = 'b'
                    elif adjacent_char == 'z':
                        replacement_char = 'y'
                    else:
                        replacement_char = chr(ord(adjacent_char) + 1)
                    for sub_idx in range(segment_start, segment_start + segment_length):
                        chars_list[sub_idx] = replacement_char
                    idx = segment_start + segment_length

        return "".join(chars_list)