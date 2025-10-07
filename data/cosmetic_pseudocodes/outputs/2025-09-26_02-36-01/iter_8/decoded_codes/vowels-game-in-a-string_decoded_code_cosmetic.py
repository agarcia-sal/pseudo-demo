class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels_set = {"a", "e", "i", "o", "u"}
        tally_odd_vowel_groups = 0
        running_vowel_tracker = 0

        iterator_index = 0
        while iterator_index < len(s):
            inspected_char = s[iterator_index]
            if inspected_char in vowels_set:
                running_vowel_tracker += 1
            iterator_index += 1

        flag_inside_odd_block = False

        index_cursor = 0
        while index_cursor < len(s):
            if s[index_cursor] in vowels_set:
                flag_inside_odd_block = not flag_inside_odd_block

            if (flag_inside_odd_block == False) and ((running_vowel_tracker % 2) == 1):
                tally_odd_vowel_groups += 1
                running_vowel_tracker = 0
            elif flag_inside_odd_block == True:
                running_vowel_tracker += 1

            index_cursor += 1

        if flag_inside_odd_block and (running_vowel_tracker % 2) == 1:
            tally_odd_vowel_groups += 1

        final_result_flag = (tally_odd_vowel_groups % 2) == 1
        return final_result_flag