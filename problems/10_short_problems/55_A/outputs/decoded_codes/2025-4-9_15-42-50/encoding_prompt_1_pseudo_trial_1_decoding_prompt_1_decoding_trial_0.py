# Start

# Read Input
inp = input()
siz = int(inp)

# Initialize Boolean List
boo = [True] * siz

# Initialize Index Variables
cur = 0
stct = 1

# Loop
while stct <= 500000:
    # Check Boolean Value
    if boo[cur]:
        boo[cur] = False
    stct += 1
    cur = (cur + stct) % siz  # Update 'cur' based on step count and to stay within bounds

# Filter Remaining True Values
rem_tr = [x for x in boo if x]  # List comprehension to filter out True values

# Check Remaining Elements
if len(rem_tr) == 0:
    print("YES")  # All marked False
else:
    print("NO")   # Some remain True

# End
