class Solution:
    def maxPointsInsideSquare(self, s):
        total = len(s)
        highest = 0
        outer_loop_index = 0
        while outer_loop_index < total:
            first_x = s[outer_loop_index][0]
            first_y = s[outer_loop_index][1]
            length_side = abs(first_x) if abs(first_x) > abs(first_y) else abs(first_y)
            marker_map = self.createEmptyAssoc()
            is_valid = True
            inner_loop_index = 0
            while True:
                if inner_loop_index >= total:
                    break
                current_x = s[inner_loop_index][0]
                current_y = s[inner_loop_index][1]
                if not (abs(current_x) > length_side or abs(current_y) > length_side):
                    current_tag = s[inner_loop_index]
                    if self.containsKey(marker_map, current_tag):
                        is_valid = False
                        break
                    else:
                        self.insertKey(marker_map, current_tag, True)
                inner_loop_index += 1
            if is_valid:
                highest = highest if highest > len(marker_map) else len(marker_map)
            outer_loop_index += 1
        return highest

    def createEmptyAssoc(self):
        return {}

    def containsKey(self, dict_, key):
        keys_list = self.getKeys(dict_)
        idx = 0
        while idx < len(keys_list):
            if keys_list[idx] == key:
                return True
            idx += 1
        return False

    def insertKey(self, dict_, key, value):
        dict_[key] = value

    def getKeys(self, dict_):
        collected = []
        counter = 0
        for pair in dict_:
            collected.append(pair)
            counter += 1
        return collected