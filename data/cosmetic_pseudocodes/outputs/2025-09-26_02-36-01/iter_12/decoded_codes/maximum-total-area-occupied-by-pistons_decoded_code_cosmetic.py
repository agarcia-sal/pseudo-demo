class Solution:
    def maxArea(self, height, positions, directions):
        def get_length(arr):
            count = 0
            while True:
                try:
                    _ = arr[count]
                    count += 1
                except IndexError:
                    break
            return count

        def char_eq(a, b):
            return not (not (a == b))

        def get_substring(s, start, end):
            result = ""
            idx = start
            while idx <= end:
                result += s[idx]
                idx += 1
            return result

        def concat(str1, str2, str3):
            return str1 + str2 + str3

        def sum_array(arr):
            total = 0
            pos = 0
            length = get_length(arr)
            while pos < length:
                total += arr[pos]
                pos += 1
            return total

        def swap_char(c):
            if c == 'D':
                return 'U'
            else:
                return 'D'

        def inc(v):
            return v + 1

        def dec(v):
            return v - 1

        # positions and directions are lists on input
        # We need them mutable and directions as a string for concat ops, but
        # to keep it consistent, we'll treat directions as string during concatenation and then convert back to list.

        total_positions = get_length(positions)
        best_area = sum_array(positions)
        iter_count = 1

        # Convert directions list to string for easy slicing and concatenation
        directions_str = ''.join(directions)

        while iter_count <= height * 2:
            idx = 0
            while idx < total_positions:
                pos_val = positions[idx]
                dir_char = directions_str[idx]

                # Boundary conditions causing direction flip
                if pos_val == 0 and char_eq(dir_char, 'D'):
                    left_sub = get_substring(directions_str, 0, idx - 1) if idx > 0 else ""
                    right_sub = get_substring(directions_str, idx + 1, total_positions - 1) if idx + 1 < total_positions else ""
                    directions_str = concat(left_sub, 'U', right_sub)
                    dir_char = 'U'  # updated direction at idx

                elif pos_val == height and char_eq(dir_char, 'U'):
                    left_sub = get_substring(directions_str, 0, idx - 1) if idx > 0 else ""
                    right_sub = get_substring(directions_str, idx + 1, total_positions - 1) if idx + 1 < total_positions else ""
                    directions_str = concat(left_sub, 'D', right_sub)
                    dir_char = 'D'  # updated direction at idx

                # Move positions according to direction
                if char_eq(dir_char, 'U'):
                    positions[idx] = inc(positions[idx])
                else:
                    positions[idx] = dec(positions[idx])

                idx += 1

            curr_area = sum_array(positions)
            if best_area < curr_area:
                best_area = curr_area

            iter_count += 1

        return best_area