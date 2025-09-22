# Initialize Input
inp = input().strip()

# Set Up Variables
ind = 0
res = ""

# Process Each Character
while ind < len(inp):
    if inp[ind] == '.':
        res += '0'
        ind += 1
    elif ind + 1 < len(inp) and inp[ind + 1] == '.':
        res += '1'
        ind += 2
    else:
        res += '2'
        ind += 2

# Display Output
print(res)
