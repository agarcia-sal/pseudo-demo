# 1. Start the program (implicit in Python by just writing code)
# 2. Read a line of input from the user and remove any surrounding whitespace
inp = input().strip()

# 3. Initialize a variable 'ind' to 0 to track our position in 'inp'
ind = 0

# 4. Initialize an empty string 'res' to build the output
res = ''

# 5. While the 'ind' is less than the length of 'inp':
while ind < len(inp):
    # 5a. If the character at 'inp[ind]' is a dot ('.'):
    if inp[ind] == '.':
        # Append '0' to 'res'
        res += '0'
        # Increment 'ind' by 1 (move to the next character)
        ind += 1
    # 5b. Else if the character following 'inp[ind]' (that is, 'inp[ind + 1]') is a dot ('.'):
    elif ind + 1 < len(inp) and inp[ind + 1] == '.':
        # Append '1' to 'res'
        res += '1'
        # Increment 'ind' by 2 (skip the next character as it is part of this pattern)
        ind += 2
    # 5c. Else:
    else:
        # Append '2' to 'res' (indicating a different pattern)
        res += '2'
        # Increment 'ind' by 2 (skip the next character as well)
        ind += 2

# 6. After processing the input string, print the 'res'
print(res)
# 7. End the program (implicit)
