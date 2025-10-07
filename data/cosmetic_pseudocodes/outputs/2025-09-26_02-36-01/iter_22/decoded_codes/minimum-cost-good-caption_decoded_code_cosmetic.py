class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        if len(caption) < 3:
            return ""

        arr = list(caption)
        x = 0
        n = len(arr)

        while x < n:
            y = x
            while x < n and arr[x] == arr[y]:
                x += 1
            z = x - y

            if z < 3:
                if y > 0 and arr[y - 1] == arr[y]:
                    arr[y - 1] = arr[y]
                    y -= 1
                    z += 1

                if x < n and arr[x - 1] == arr[x]:
                    arr[x] = arr[x - 1]
                    x += 1
                    z += 1

                if z < 3:
                    if y > 0:
                        c = arr[y - 1]
                    else:
                        c = arr[x] if x < n else arr[y]

                    if c == 'a':
                        c = 'b'
                    elif c == 'z':
                        c = 'y'
                    else:
                        c = chr(ord(c) + 1)

                    for index in range(y, y + z):
                        arr[index] = c

                    x = y + z

        return "".join(arr)