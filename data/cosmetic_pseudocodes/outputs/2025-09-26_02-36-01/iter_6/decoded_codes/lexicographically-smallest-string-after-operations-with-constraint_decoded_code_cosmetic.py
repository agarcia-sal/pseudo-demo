class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            distance_forward = abs(ord(c1) - ord(c2))
            distance_backward = 26 - distance_forward
            return distance_forward if distance_forward <= distance_backward else distance_backward

        char_list = list(s)
        length_s = len(s)
        k_remaining = k

        def process_characters(current_pos: int) -> None:
            nonlocal k_remaining
            if k_remaining <= 0 or current_pos >= length_s:
                return

            if char_list[current_pos] == 'a':
                process_characters(current_pos + 1)
                return

            dist_to_a = cyclic_distance(char_list[current_pos], 'a')
            if dist_to_a <= k_remaining:
                char_list[current_pos] = 'a'
                k_remaining -= dist_to_a
            else:
                original_code = ord(char_list[current_pos])
                char_list[current_pos] = chr(original_code - k_remaining)
                k_remaining = 0

            process_characters(current_pos + 1)

        process_characters(0)

        result_string = ''
        for rev_idx in range(length_s - 1, -1, -1):
            result_string = char_list[rev_idx] + result_string

        return result_string