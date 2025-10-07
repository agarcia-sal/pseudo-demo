class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def tallyElements(input_string):
            result_map = {}
            position = 0
            while position < len(input_string):
                symbol = input_string[position]
                if symbol in result_map:
                    result_map[symbol] += 1
                else:
                    result_map[symbol] = 1
                position += 1
            return result_map

        tally_map = tallyElements(s)
        if '?' in tally_map:
            del tally_map['?']

        indices_of_questions = []
        idx_counter = 0
        while idx_counter < len(s):
            if s[idx_counter] == '?':
                indices_of_questions.append(idx_counter)
            idx_counter += 1

        candidates = []

        def alphabetSequence():
            letters = []
            num = 97
            while num <= 122:
                letters.append(chr(num))
                num += 1
            return letters

        def getCount(key, mapping):
            return mapping.get(key, 0)

        def findMinimalChar(count_map):
            minimal_value = 1e9
            minimal_character = None
            for letter in alphabetSequence():
                count_for_letter = getCount(letter, count_map)
                if count_for_letter < minimal_value:
                    minimal_value = count_for_letter
                    minimal_character = letter
            return minimal_character, minimal_value

        for _ in range(len(indices_of_questions)):
            current_min_char = None
            current_min_val = float('inf')
            for ch in alphabetSequence():
                current_count = getCount(ch, tally_map)
                if current_count < current_min_val:
                    current_min_val = current_count
                    current_min_char = ch
            candidates.append(current_min_char)
            tally_map[current_min_char] = tally_map.get(current_min_char, 0) + 1

        def sortListAscending(list_data):
            n = len(list_data)
            if n <= 1:
                return
            i = 0
            while i < n - 1:
                j = 0
                while j < n - i - 1:
                    if list_data[j] > list_data[j + 1]:
                        temp = list_data[j]
                        list_data[j] = list_data[j + 1]
                        list_data[j + 1] = temp
                    j += 1
                i += 1

        sortListAscending(candidates)

        mutable_s = []
        pointer = 0
        while pointer < len(s):
            mutable_s.append(s[pointer])
            pointer += 1

        cursor = 0
        while cursor < len(indices_of_questions):
            substitution_index = indices_of_questions[cursor]
            mutable_s[substitution_index] = candidates[cursor]
            cursor += 1

        def joinCharacters(arr):
            composed = ""
            i = 0
            while i < len(arr):
                composed += arr[i]
                i += 1
            return composed

        return joinCharacters(mutable_s)