# Step 1: Get Input
fir = input()  # Read first string
sec = input()  # Read second string

# Step 2: Remove Spaces
cle1 = fir.replace(" ", "")  # Create 'cle1' by removing spaces from 'fir'
cle2 = sec.replace(" ", "")  # Create 'cle2' by removing spaces from 'sec'

# Step 3: Count Character Frequencies
dif = []  # Initialize an empty list 'dif' to store frequency differences
for char in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    count1 = cle1.count(chr(char))  # Count occurrences of the character in 'cle1'
    count2 = cle2.count(chr(char))  # Count occurrences of the character in 'cle2'
    dif.append(count1 - count2)  # Append the result to 'dif'

# Step 4: Evaluate Character Counts
if all(d >= 0 for d in dif):  # Check if there are any negative values in 'dif'
    print("YES")  # All characters in 'sec' are covered
else:
    print("NO")  # Some characters in 'sec' are not covered by 'fir'
