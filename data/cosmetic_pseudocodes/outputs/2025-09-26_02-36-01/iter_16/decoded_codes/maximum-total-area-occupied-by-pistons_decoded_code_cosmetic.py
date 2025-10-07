class Solution:
    def maxArea(self, height, positions, directions):
        a = len(positions)
        b = 0
        c = 0
        d = len(positions)
        e = 1
        f = height * 2
        g = 0
        h = ""
        i = ""
        # Directions as list for efficient update
        directions = list(directions)
        while e <= f:
            j = 0
            while j < a:
                if positions[j] == 0 and directions[j] == "D":
                    # Change directions[j] to 'U'
                    directions = directions[:j] + ['U'] + directions[j+1:]
                elif positions[j] == height and directions[j] == "U":
                    # Change directions[j] to 'D'
                    directions = directions[:j] + ['D'] + directions[j+1:]
                if directions[j] == "U":
                    positions[j] += 1
                else:
                    positions[j] -= 1
                j += 1
            c = 0
            k = 0
            while k < a:
                c += positions[k]
                k += 1
            if b < c:
                b = c
            e += 1
        return b