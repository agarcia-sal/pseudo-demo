class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        m = len(caption)
        if not (m >= 3):
            return ""

        chars_list = list(caption)

        def extendSegment(idx, cap_list):
            if idx >= m:
                return idx
            seg_start = idx

            def advance(k):
                if k < m and cap_list[k] == cap_list[seg_start]:
                    return advance(k + 1)
                else:
                    return k

            return advance(idx)

        def fillWithChar(lst, start_pos, length_seg, fill_char):
            def recurFill(pos):
                if pos >= start_pos + length_seg:
                    return
                lst[pos] = fill_char
                recurFill(pos + 1)
            recurFill(start_pos)

        def nextAlphaCharacter(ch):
            if ch == 'a':
                return 'b'
            elif ch == 'z':
                return 'y'
            else:
                return chr(ord(ch) + 1)

        current_pos = 0
        while current_pos < m:
            segment_end = extendSegment(current_pos, chars_list)
            segment_length = segment_end - current_pos

            if segment_length < 3:
                if (current_pos - 1) >= 0 and chars_list[current_pos - 1] == chars_list[current_pos]:
                    chars_list[current_pos - 1] = chars_list[current_pos]
                    current_pos -= 1
                    segment_length += 1

                if segment_end < m and chars_list[segment_end - 1] == chars_list[segment_end]:
                    chars_list[segment_end] = chars_list[segment_end - 1]
                    segment_end += 1
                    segment_length += 1

                if segment_length < 3:
                    if (current_pos - 1) >= 0:
                        replacement_char = chars_list[current_pos - 1]
                    else:
                        replacement_char = chars_list[segment_end]

                    if replacement_char == 'a':
                        replacement_char = 'b'
                    elif replacement_char == 'z':
                        replacement_char = 'y'
                    else:
                        replacement_char = nextAlphaCharacter(replacement_char)

                    fillWithChar(chars_list, current_pos, segment_length, replacement_char)
                    current_pos += segment_length
                else:
                    current_pos = segment_end
            else:
                current_pos = segment_end

        return "".join(chars_list)