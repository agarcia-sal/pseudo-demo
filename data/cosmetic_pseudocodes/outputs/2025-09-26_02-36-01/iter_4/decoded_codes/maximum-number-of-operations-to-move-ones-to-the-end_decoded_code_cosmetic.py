class Solution:
    def maxOperations(self, collection):
        result = 0
        tally = 0
        cursor = 0
        while cursor < len(collection):
            current_char = collection[cursor]
            if current_char == '1':
                tally += 1
            else:
                if cursor != 0:
                    previous_char = collection[cursor - 1]
                    if previous_char == '1':
                        result += tally
            cursor += 1
        return result