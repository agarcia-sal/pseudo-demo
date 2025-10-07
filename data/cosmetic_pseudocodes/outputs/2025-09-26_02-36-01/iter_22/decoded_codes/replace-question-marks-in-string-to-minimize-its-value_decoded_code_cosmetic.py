class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def helper_increment(map_var: dict, key_var: str) -> None:
            if key_var in map_var:
                map_var[key_var] += 1
            else:
                map_var[key_var] = 1

        def helper_find_min_key(freq_map: dict) -> str:
            minimal_value = float('inf')
            minimal_key = None
            alphabet_set = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            index_var = 0
            while index_var < len(alphabet_set):
                current_key = alphabet_set[index_var]
                current_value = freq_map.get(current_key, 0)
                if current_value < minimal_value:
                    minimal_value = current_value
                    minimal_key = current_key
                index_var += 1
            return minimal_key

        freq_map = {}
        position_var = 0
        while position_var < len(s):
            char_var = s[position_var]
            if char_var != "?":
                if char_var in freq_map:
                    freq_map[char_var] += 1
                else:
                    freq_map[char_var] = 1
            position_var += 1

        question_positions = []
        cursor_var = 0
        while True:
            if cursor_var >= len(s):
                break
            current_character = s[cursor_var]
            if current_character == "?":
                question_positions.append(cursor_var)
            cursor_var += 1

        replacement_array = []
        iter_var = 0
        while iter_var < len(question_positions):
            minimal_character = helper_find_min_key(freq_map)
            replacement_array.append(minimal_character)
            helper_increment(freq_map, minimal_character)
            iter_var += 1

        temp_list = []
        idx_var = 0
        while idx_var < len(s):
            temp_list.append(s[idx_var])
            idx_var += 1

        xx = 0
        while xx < len(question_positions):
            temp_list[question_positions[xx]] = replacement_array[xx]
            xx += 1

        result_str = ""
        yy = 0
        while yy < len(temp_list):
            result_str += temp_list[yy]
            yy += 1

        return result_str