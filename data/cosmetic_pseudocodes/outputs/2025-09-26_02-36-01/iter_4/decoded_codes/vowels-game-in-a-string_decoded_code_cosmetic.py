class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_chars = {'a', 'e', 'i', 'o', 'u'}
        segment_count = 0
        running_count = 0

        position = 0
        length_of_s = len(s)
        # Count total vowels in the string
        while position < length_of_s:
            current_char = s[position]
            is_vowel = False
            check_index = 0
            vowels_length = len(vowel_chars)
            while check_index < vowels_length:
                # since vowel_chars is a set, convert to list for indexing
                if current_char == list(vowel_chars)[check_index]:
                    is_vowel = True
                    break
                check_index += 1
            if is_vowel:
                running_count += 1
            position += 1

        inside_odd_segment = False

        index = 0
        while index < length_of_s:
            letter = s[index]
            vowel_found = False
            search_index = 0
            vowels_length = len(vowel_chars)
            while search_index < vowels_length:
                if letter == list(vowel_chars)[search_index]:
                    vowel_found = True
                    break
                search_index += 1
            if vowel_found:
                inside_odd_segment = not inside_odd_segment

            running_count_mod2 = running_count - 2 * (running_count // 2)
            if (not inside_odd_segment) and running_count_mod2 == 1:
                segment_count += 1
                running_count = 0
            elif inside_odd_segment:
                running_count += 1
            index += 1

        remainder_mod2 = running_count - 2 * (running_count // 2)
        if inside_odd_segment and remainder_mod2 == 1:
            segment_count += 1

        final_result = False
        if segment_count - 2 * (segment_count // 2) == 1:
            final_result = True

        return final_result