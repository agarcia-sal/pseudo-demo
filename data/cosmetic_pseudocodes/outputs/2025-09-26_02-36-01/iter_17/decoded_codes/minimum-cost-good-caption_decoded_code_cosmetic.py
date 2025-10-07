class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        length = len(caption)
        if length < 3:
            return ""

        chars = list(caption)
        i = 0

        while True:
            if not (i < length):
                break

            start = i
            # Move i forward while characters equal to chars[start]
            while i < length and chars[i] == chars[start]:
                i += 1

            count = i - start

            if count >= 3:
                # Already 3 or more, continue to next run
                continue

            # Try to expand run backward if previous character same
            if start > 0 and chars[start - 1] == chars[start]:
                start -= 1
                count += 1

            # Try to expand run forward if next character same
            if i < length and chars[i - 1] == chars[i]:
                chars[i] = chars[i - 1]
                i += 1
                count += 1

            if count >= 3:
                # After adjustment, if >=3 continue
                continue

            # Determine replacement character n940a
            if start > 0:
                n940a = chars[start - 1]
            else:
                # If no previous, take next char if exists, else just chars[start]
                n940a = chars[i] if i < length else chars[start]

            # Adjust n940a according to the rules
            if n940a == 'a':
                n940a = 'b'
            elif n940a == 'z':
                n940a = 'y'
            else:
                n940a = chr(ord(n940a) + 1)

            # Replace the run [start, start + count - 1] with n940a
            for idx in range(start, start + count):
                chars[idx] = n940a

            i = start + count

        return ''.join(chars)