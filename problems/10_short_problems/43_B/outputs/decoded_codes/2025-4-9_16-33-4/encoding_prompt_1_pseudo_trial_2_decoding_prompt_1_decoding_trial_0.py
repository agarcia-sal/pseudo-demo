# START

# Step 1: Read two lines of input
CHARACTERS_FROM_FIRST_LINE = input()
SECOND_LINE = input()

# Step 2: Process the input to eliminate spaces
CH1 = CHARACTERS_FROM_FIRST_LINE.replace(" ", "")
CH2 = SECOND_LINE.replace(" ", "")

# Step 3: Initialize a list to keep track of character frequencies
FRE_DIF = []

# Step 4: Calculate frequency differences for each character from 'A' to 'z'
for CHARACTER_CODE in range(ord('A'), ord('z') + 1):
    CT1 = CH1.count(chr(CHARACTER_CODE))
    CT2 = CH2.count(chr(CHARACTER_CODE))
    DIFFERENCE = CT1 - CT2
    FRE_DIF.append(DIFFERENCE)

# Step 5: Check if any frequency difference is negative
NGCT = sum(1 for x in FRE_DIF if x < 0)

# Step 6: Determine the output based on the negative count
if NGCT == 0:
    print("YES")  # All characters in the first string are matched or exceeded in the second string
else:
    print("NO")   # Some characters in the first string are not matched in the second string

# END
