class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        idx = 0
        acc_len = 1
        accumulator = []

        while idx < len(operations):
            accumulator.append(operations[idx])
            acc_len += acc_len  # equivalent to acc_len = acc_len * 2
            idx += 1

        current_char = 'a'
        position = len(accumulator) - 1

        while position >= 0:
            half_len = acc_len // 2
            if k > half_len:
                k -= half_len
                acc_len = half_len
                if accumulator[position] == 1:
                    # increment character with wrap from 'z' to 'a'
                    if current_char == 'z':
                        current_char = 'a'
                    else:
                        current_char = chr(ord(current_char) + 1)
            else:
                acc_len = half_len
            position -= 1

        return current_char