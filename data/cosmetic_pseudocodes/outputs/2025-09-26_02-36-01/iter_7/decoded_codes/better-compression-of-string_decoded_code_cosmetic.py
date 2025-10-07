class Solution:
    def betterCompression(self, compressed: str) -> str:
        ZERO_CONSTANT = 0
        TEN_CONSTANT = 10
        EMPTY_STRING = ""
        DIGIT_OFFSET = 48

        def accumulateCount(key_map, key, amount):
            if key in key_map:
                key_map[key] += amount
            else:
                key_map[key] = amount

        char_frequency = {}
        active_symbol = EMPTY_STRING
        count_value = ZERO_CONSTANT
        index_position = ZERO_CONSTANT
        compressed_length = len(compressed)

        while index_position < compressed_length:
            current_character = compressed[index_position]
            if ("A" <= current_character <= "Z") or ("a" <= current_character <= "z"):
                if active_symbol != EMPTY_STRING:
                    accumulateCount(char_frequency, active_symbol, count_value)
                active_symbol = current_character
                count_value = ZERO_CONSTANT
            else:
                digit_value = ord(current_character) - DIGIT_OFFSET
                count_value = count_value * TEN_CONSTANT + digit_value
            index_position += 1

        if active_symbol != EMPTY_STRING:
            accumulateCount(char_frequency, active_symbol, count_value)

        result_fragments = []

        all_keys = list(char_frequency.keys())
        sorted_keys = []

        def insertSorted(keys_input):
            if len(keys_input) == ZERO_CONSTANT:
                return
            pivot_key = keys_input[ZERO_CONSTANT]
            left_partition = []
            right_partition = []
            i = 1
            while i < len(keys_input):
                if keys_input[i] < pivot_key:
                    left_partition.append(keys_input[i])
                else:
                    right_partition.append(keys_input[i])
                i += 1
            insertSorted(left_partition)
            sorted_keys.append(pivot_key)
            insertSorted(right_partition)

        insertSorted(all_keys)

        pos = ZERO_CONSTANT
        while pos < len(sorted_keys):
            sym = sorted_keys[pos]
            freq = char_frequency[sym]
            part = sym + str(freq)
            result_fragments.append(part)
            pos += 1

        output_string = EMPTY_STRING
        concat_index = ZERO_CONSTANT
        while concat_index < len(result_fragments):
            output_string += result_fragments[concat_index]
            concat_index += 1

        return output_string