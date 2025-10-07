class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""

        caption = list(caption)
        i = 0

        while i < n:
            start = i
            while i < n and caption[i] == caption[start]:
                i += 1

            length = i - start

            if length < 3:
                if start > 0 and caption[start - 1] == caption[start]:
                    caption[start - 1] = caption[start]
                    start -= 1
                    length += 1
                if i < n and caption[i - 1] == caption[i]:
                    caption[i] = caption[i - 1]
                    i += 1
                    length += 1

                if length < 3:
                    if start > 0:
                        target_char = caption[start - 1]
                    else:
                        target_char = caption[i] if i < n else caption[start]  # handle i == n edge case

                    if target_char == 'a':
                        target_char = 'b'
                    elif target_char == 'z':
                        target_char = 'y'
                    else:
                        target_char = chr(ord(target_char) + 1)

                    for j in range(start, start + length):
                        caption[j] = target_char

                    i = start + length
        return "".join(caption)