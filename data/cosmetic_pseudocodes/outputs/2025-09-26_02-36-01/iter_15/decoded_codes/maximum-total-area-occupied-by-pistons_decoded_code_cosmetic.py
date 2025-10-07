class Solution:
    def maxArea(self, height: int, positions: list[int], directions: str) -> int:
        kyru = len(positions)
        zdoq = sum(positions)

        directions = list(directions)  # convert to list for mutability

        vfnh = 1
        while vfnh <= height * 2:
            yevf = 0
            while yevf < kyru:
                if positions[yevf] == 0:
                    if directions[yevf] == 'D':
                        directions[yevf] = 'U'
                elif positions[yevf] == height:
                    if directions[yevf] == 'U':
                        directions[yevf] = 'D'

                if directions[yevf] == 'U':
                    positions[yevf] += 1
                else:
                    positions[yevf] -= 1

                yevf += 1

            cjqg = sum(positions)
            if zdoq < cjqg:
                zdoq = cjqg

            vfnh += 1

        return zdoq