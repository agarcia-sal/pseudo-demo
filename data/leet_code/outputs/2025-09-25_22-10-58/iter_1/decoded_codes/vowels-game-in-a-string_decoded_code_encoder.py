class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        odd_vowel_segments = 0
        current_vowel_count = 0

        # Count total vowels
        for char in s:
            if char in vowels:
                current_vowel_count += 1

        in_odd_segment = False

        for char in s:
            if char in vowels:
                in_odd_segment = not in_odd_segment
            if not in_odd_segment and current_vowel_count % 2 == 1:
                odd_vowel_segments += 1
                current_vowel_count = 0
            elif in_odd_segment:
                current_vowel_count += 1

        if in_odd_segment and current_vowel_count % 2 == 1:
            odd_vowel_segments += 1

        return odd_vowel_segments % 2 == 1