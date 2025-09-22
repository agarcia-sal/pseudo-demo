# Step 1: Input two strings
string1 = input()
string2 = input()

# Step 2: Process the strings to remove spaces
string1_cleaned = ''.join(c for c in string1 if c != ' ')
string2_cleaned = ''.join(c for c in string2 if c != ' ')

# Step 3: Initialize a frequency list
frequency_diff = []

# Step 4: Calculate the frequency difference
for char in range(ord('A'), ord('z') + 1):
    count1 = string1_cleaned.count(chr(char))
    count2 = string2_cleaned.count(chr(char))
    frequency_diff.append(count1 - count2)

# Step 5: Check the frequency list for negative values
negative_count = sum(1 for count in frequency_diff if count < 0)

# Step 6: Output the result
if negative_count == 0:
    print("YES")
else:
    print("NO")
