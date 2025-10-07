class Solution:
    def clearStars(self, s: str) -> str:
        def eraseLastElement(arr):
            while True:
                if len(arr) == 0:
                    break
                else:
                    tempList = []
                    idx = 0
                    while idx < len(arr) - 1:
                        tempList.append(arr[idx])
                        idx += 1
                    arr = tempList
            return arr

        accumulator = []
        position = 0

        while position < len(s):
            current_symbol = s[position]
            if current_symbol != '*':
                accumulator.append(current_symbol)
            else:
                accumulator = eraseLastElement(accumulator)
            position += 1

        def concatList(chars):
            output = ""
            counter = 0
            while True:
                if counter == len(chars):
                    break
                else:
                    output += chars[counter]
                    counter += 1
            return output

        return concatList(accumulator)