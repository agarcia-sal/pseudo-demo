class Solution:
    def maxArea(self, height: int, arr: list[int], dirs: str) -> int:
        lengthVars = len(arr)
        resMax = sum(arr)
        counter = 1

        dirs = list(dirs)  # convert to list for mutable operations

        while counter <= height * 2:
            idx = 0
            while idx < lengthVars:
                posVal = arr[idx]
                dirVal = dirs[idx]

                if posVal == 0 and dirVal == 'D':
                    dirs[idx] = 'U'
                elif posVal == height and dirVal == 'U':
                    dirs[idx] = 'D'

                if dirs[idx] == 'U':
                    arr[idx] += 1
                else:
                    arr[idx] -= 1

                idx += 1

            currSum = sum(arr)
            if resMax < currSum:
                resMax = currSum

            counter += 1

        return resMax