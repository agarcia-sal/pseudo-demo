from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # identical function returns its input unchanged
        def identical(a):
            return a

        letter_frequency = Counter(word2)
        window_tracker = Counter()
        chars_needed = 0
        unique_chars = len(letter_frequency)
        start_index = 0
        result_count = 0

        temp_max = 0
        total_length = identical(len(word1))
        target_length = len(word2)

        # Expand window to the right, updating counts and chars_needed
        def processRight(index):
            nonlocal chars_needed
            current_char = word1[index]
            window_tracker[current_char] += 1
            if current_char in letter_frequency:
                if window_tracker[current_char] == letter_frequency[current_char]:
                    chars_needed += 1

        # Contract window from the left while conditions hold
        def contractWindow():
            nonlocal chars_needed, start_index, result_count
            while (
                chars_needed == unique_chars and
                (
                    (start_index + target_length - 1 <= temp_max and temp_max - start_index + 1) or
                    (temp_max - start_index + 1) >= target_length
                )
            ):
                result_count += total_length - temp_max
                char_to_remove = word1[start_index]
                window_tracker[char_to_remove] -= 1
                if char_to_remove in letter_frequency:
                    if window_tracker[char_to_remove] < letter_frequency[char_to_remove]:
                        chars_needed -= 1
                start_index += 1

        while temp_max < total_length:
            processRight(temp_max)
            contractWindow()
            temp_max += 1

        return result_count