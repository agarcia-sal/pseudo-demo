class Solution:
    def clearStars(self, s: str) -> str:
        temp_storage = []
        index = 0
        while index < len(s):
            current_char = s[index]
            if current_char == "*":
                if temp_storage:
                    temp_storage.pop()
            else:
                temp_storage.append(current_char)
            index += 1

        ptr = 0

        def concatAll():
            nonlocal ptr
            if ptr == len(temp_storage):
                return ""
            result = temp_storage[ptr]
            ptr += 1
            return result + concatAll()

        return concatAll()