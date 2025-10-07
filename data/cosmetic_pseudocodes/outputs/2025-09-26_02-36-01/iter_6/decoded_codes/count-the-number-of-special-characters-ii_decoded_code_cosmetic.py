class Solution:
    class KeyValue:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def numberOfSpecialChars(self, word: str) -> int:
        def containsKey(collection, keyToFind) -> bool:
            idx_checker = 0
            found_flag = False
            keys_list = getKeys(collection)
            while idx_checker < len(keys_list) and not found_flag:
                if keys_list[idx_checker] == keyToFind:
                    found_flag = True
                idx_checker += 1
            return found_flag

        def getKeys(coll) -> list:
            key_accum = []
            idx_col = 0
            while idx_col < len(coll):
                key_accum.append(coll[idx_col].key)
                idx_col += 1
            return key_accum

        def zipLists(list1, list2) -> list:
            zipped_result = []
            idx_zip = 0
            min_length = len(list1)
            if len(list2) < min_length:
                min_length = len(list2)
            while idx_zip < min_length:
                zipped_result.append((list1[idx_zip], list2[idx_zip]))
                idx_zip += 1
            return zipped_result

        key_positions_first = []
        key_positions_last = []

        position_counter = 0
        length_word = len(word)

        while position_counter < length_word:
            current_letter = word[position_counter]
            if not containsKey(key_positions_first, current_letter):
                key_positions_first.append(self.KeyValue(current_letter, position_counter))

            last_index = 0
            found_in_last = False
            keys_last = getKeys(key_positions_last)
            while last_index < len(keys_last) and not found_in_last:
                if keys_last[last_index] == current_letter:
                    key_positions_last[last_index].value = position_counter
                    found_in_last = True
                last_index += 1

            if not found_in_last:
                key_positions_last.append(self.KeyValue(current_letter, position_counter))

            position_counter += 1

        count_special = 0

        lower_alphabet = list('abcdefghijklmnopqrstuvwxyz')
        upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        pairs_list = zipLists(lower_alphabet, upper_alphabet)

        idx_pair = len(pairs_list) - 1

        while idx_pair >= 0:
            lower_char = pairs_list[idx_pair][0]
            upper_char = pairs_list[idx_pair][1]

            found_in_last_upper = containsKey(key_positions_last, lower_char)
            found_in_first_lower = containsKey(key_positions_first, upper_char)

            if found_in_last_upper and found_in_first_lower:
                pos_last = 0
                pos_first = 0
                last_found = False
                first_found = False

                while pos_last < len(key_positions_last) and not last_found:
                    if key_positions_last[pos_last].key == lower_char:
                        last_found = True
                    else:
                        pos_last += 1

                while pos_first < len(key_positions_first) and not first_found:
                    if key_positions_first[pos_first].key == upper_char:
                        first_found = True
                    else:
                        pos_first += 1

                last_value = key_positions_last[pos_last].value
                first_value = key_positions_first[pos_first].value

                if last_value < first_value:
                    count_special += 1

            idx_pair -= 1

        return count_special