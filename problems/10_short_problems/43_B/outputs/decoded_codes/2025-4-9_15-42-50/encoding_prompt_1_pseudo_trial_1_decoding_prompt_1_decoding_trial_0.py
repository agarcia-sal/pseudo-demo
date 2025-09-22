# 1. Get Input
fir = input()  # Read first string
sec = input()  # Read second string

# 2. Remove Spaces
cle1 = fir.replace(" ", "")  # Create 'cle1' by removing all spaces
cle2 = sec.replace(" ", "")  # Create 'cle2' by removing all spaces

# 3. Count Character Frequencies
dif = []  # Initialize an empty list for frequency differences
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    char = chr(ascii_value)  # Get the character from ASCII value
    count_cle1 = cle1.count(char)  # Count occurrences in 'cle1'
    count_cle2 = cle2.count(char)  # Count occurrences in 'cle2'
    dif.append(count_cle1 - count_cle2)  # Append frequency difference to 'dif'

# 4. Evaluate Character Counts
if all(diff >= 0 for diff in dif):  # Check if all values in 'dif' are non-negative
    print("YES")  # Print "YES" if all characters in 'sec' are covered by 'fir'
else:
    print("NO")  # Print "NO" if there are characters in 'sec' not covered by 'fir'
