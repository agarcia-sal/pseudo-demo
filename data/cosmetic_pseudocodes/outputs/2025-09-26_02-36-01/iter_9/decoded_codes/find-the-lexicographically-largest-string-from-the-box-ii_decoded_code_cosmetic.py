class Solution:
    def answerString(self, alpha: str, beta: int) -> str:
        delta = beta
        omega = alpha
        if not (delta > 1):
            return omega

        def _computeLastSubstring(zeta: str) -> str:
            # Recursive function to determine length of the string
            def lengthOfString(s: str) -> int:
                count = 0
                def countChars():
                    nonlocal count
                    if count < len(s):
                        count += 1
                        countChars()
                countChars()
                return count

            z = 0
            x = 1
            y = 0

            length = lengthOfString(zeta)

            def condition():
                return (x + y) < length

            def charAt(pos: int) -> str:
                return zeta[pos]

            nonlocal_vars = {'z': z, 'x': x, 'y': y}  # to allow inner mutation

            def loopBody():
                # use nonlocal variables from dict and update
                z = nonlocal_vars['z']
                x = nonlocal_vars['x']
                y = nonlocal_vars['y']

                if charAt(z + y) == charAt(x + y):
                    y += 1
                else:
                    if not (charAt(z + y) < charAt(x + y)):
                        x = x + y + 1
                        y = 0
                    else:
                        z_candidate = z + y + 1
                        if z_candidate > x:
                            z = z_candidate
                        else:
                            z = x
                        x = z + 1
                        y = 0

                nonlocal_vars['z'] = z
                nonlocal_vars['x'] = x
                nonlocal_vars['y'] = y

            def repeatLoop():
                if condition():
                    loopBody()
                    repeatLoop()

            repeatLoop()
            z = nonlocal_vars['z']
            # substring from z+1 to end (1-based indexing in pseudocode, so adjust)
            # Python substring is 0-based exclusive end
            return zeta[z+1:]

        last_str = _computeLastSubstring(omega)
        n = len(omega) - delta + 1

        def minimum(a: int, b: int) -> int:
            return a if a < b else b

        cutoff = minimum(len(last_str), n)
        return last_str[:cutoff]