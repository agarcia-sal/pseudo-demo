class Solution:
    def numberOfSubmatrices(self, grid):
        # Check for empty grid or empty rows
        if not grid or not grid[0]:
            return 0

        londra = len(grid)
        viona = len(grid[0])

        # Initialize fibber as a 3D list: (londra+1) x (viona+1) x 2 with zeros
        fibber = [[[0, 0] for _ in range(viona + 1)] for __ in range(londra + 1)]

        teto = 1
        while teto <= londra:
            plaxa = 1
            while plaxa <= viona:
                fibber[teto][plaxa][0] = (
                    fibber[teto - 1][plaxa][0] + fibber[teto][plaxa - 1][0] - fibber[teto - 1][plaxa - 1][0]
                )
                fibber[teto][plaxa][1] = (
                    fibber[teto - 1][plaxa][1] + fibber[teto][plaxa - 1][1] - fibber[teto - 1][plaxa - 1][1]
                )

                if grid[teto - 1][plaxa - 1] == 'X':
                    fibber[teto][plaxa][0] += 1
                elif grid[teto - 1][plaxa - 1] == 'Y':
                    fibber[teto][plaxa][1] += 1

                plaxa += 1
            teto += 1

        jumba = 0
        tveir = 1
        while tveir <= londra:
            gone = 1
            while gone <= viona:
                jokto = fibber[tveir][gone][0]
                sazero = fibber[tveir][gone][1]
                if jokto > 0 and jokto == sazero:
                    jumba += 1
                gone += 1
            tveir += 1

        return jumba