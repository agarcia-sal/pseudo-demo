class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(x: str, y: str) -> int:
            temp1 = abs(ord(x) - ord(y))
            temp2 = 26 - temp1
            return temp1 if temp1 < temp2 else temp2

        alpha_array = list(s)
        pointer = 0
        length = len(s)

        def proceed_loop():
            nonlocal k, pointer
            if k > 0 and pointer < length:
                if alpha_array[pointer] == 'a':
                    pointer += 1
                    proceed_loop()
                else:
                    distance_calc = cyclic_distance(alpha_array[pointer], 'a')
                    if distance_calc <= k:
                        alpha_array[pointer] = 'a'
                        k -= distance_calc
                    else:
                        # shift character k steps backwards
                        new_char = chr(ord(alpha_array[pointer]) - k)
                        alpha_array[pointer] = new_char
                        k = 0
                    pointer += 1
                    proceed_loop()

        proceed_loop()
        return ''.join(alpha_array)