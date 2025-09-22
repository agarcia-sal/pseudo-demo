# Step 1: Read two lines of input
FIRST_LINE = input()
SECOND_LINE = input()

# Step 2: Process the input to eliminate spaces
CHARACTERS_FROM_FIRST_LINE = FIRST_LINE.replace(" ", "")
CHARACTERS_FROM_SECOND_LINE = SECOND_LINE.replace(" ", "")

# Step 3: Initialize a list to keep track of character frequencies
FREQUENCY_DIFFERENCE = []

# Step 4: Calculate frequency differences for each character from 'A' to 'z'
for CHARACTER_CODE in range(ord('A'), ord('z') + 1):
    CHARACTER = chr(CHARACTER_CODE)
    COUNT_IN_FIRST_LINE = CHARACTERS_FROM_FIRST_LINE.count(CHARACTER)
    COUNT_IN_SECOND_LINE = CHARACTERS_FROM_SECOND_LINE.count(CHARACTER)
    DIFFERENCE = COUNT_IN_FIRST_LINE - COUNT_IN_SECOND_LINE
    FREQUENCY_DIFFERENCE.append(DIFFERENCE)

# Step 5: Check if any frequency difference is negative
NEGATIVE_COUNT = sum(1 for diff in FREQUENCY_DIFFERENCE if diff < 0)

# Step 6: Determine the output based on the negative count
if NEGATIVE_COUNT == 0:
    print("YES")  # All characters in the first string are matched or exceeded in the second string
else:
    print("NO")   # Some characters in the first string are not matched in the second string
