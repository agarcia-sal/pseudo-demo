# Begin Program

# Step 2: Initialize two lists to store non-space characters from the inputs
s1 = []
s2 = []

# Step 4: Read first input and store it in variable 'first_input'
first_input = input()

# Step 5: Read second input and store it in variable 'second_input'
second_input = input()

# Step 6-7: Process first input
for character in first_input:
    # Step 6a: If the character is not a space
    if character != ' ':
        # Step 6ai: Add the character to list s1
        s1.append(character)

# Step 8: Process second input
for character in second_input:
    # Step 7a: If the character is not a space
    if character != ' ':
        # Step 7ai: Add the character to list s2
        s2.append(character)

# Step 8: Initialize a list to store frequency differences
freqs = []

# Step 9: Count frequency differences for each character from 'A' to 'z'
for x in range(ord('A'), ord('z') + 1):
    # Step 9a: Count occurrences in s1
    count_s1 = s1.count(chr(x))
    # Step 9b: Count occurrences in s2
    count_s2 = s2.count(chr(x))
    # Step 9c: Calculate the frequency difference
    freq_diff = count_s1 - count_s2
    # Step 9d: Store the result in freqs
    freqs.append(freq_diff)

# Step 10: Count the number of negative elements in freqs
negative_count = sum(1 for freq in freqs if freq < 0)

# Step 11: Check the count of negative frequencies
if negative_count == 0:
    # Step 11a: Output "YES"
    print("YES")
else:
    # Step 12a: Output "NO"
    print("NO")

# End Program
