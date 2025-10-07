class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        length_s = len(s)

        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_value(x: int) -> int:
                return -x if x < 0 else x

            diff = abs_value(ord(c1) - ord(c2))
            complement = 26 - diff
            return diff if diff < complement else complement

        characters = list(s)
        position = 0

        def reduce_to_a_at(pos: int, rem: int, arr: list[str]) -> int:
            if rem < 1 or pos >= length_s:
                return rem
            if arr[pos] == 'a':
                return reduce_to_a_at(pos + 1, rem, arr)

            distance = cyclic_distance(arr[pos], 'a')
            if distance <= rem:
                arr[pos] = 'a'
                return reduce_to_a_at(pos + 1, rem - distance, arr)
            else:
                arr[pos] = chr(ord(arr[pos]) - rem)
                return 0

        remaining = reduce_to_a_at(position, k, characters)

        def reconstruct_string(arr: list[str]) -> str:
            output = ""
            idx = 0
            while idx < len(arr):
                output += arr[idx]
                idx += 1
            return output

        return reconstruct_string(characters)