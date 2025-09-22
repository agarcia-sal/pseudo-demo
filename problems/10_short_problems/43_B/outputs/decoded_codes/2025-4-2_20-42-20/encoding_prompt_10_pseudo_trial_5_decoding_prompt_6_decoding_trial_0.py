# Step 1: Receive Input
string_one = input()  # input for the first string
string_two = input()  # input for the second string

# Step 2: Initialize Variables
cleaned_string_one = string_one.replace(" ", "")  # removing spaces from the first string
cleaned_string_two = string_two.replace(" ", "")  # removing spaces from the second string

# Step 3: Initialize Frequency List
character_frequencies = []  # list to hold frequency differences

# Step 4: Calculate Character Frequencies
for char_code in range(65, 123):  # ASCII values for 'A' (65) to 'z' (122)
    char = chr(char_code)  # converting ASCII code to character
    freq_difference = cleaned_string_one.count(char) - cleaned_string_two.count(char)  # frequency difference
    character_frequencies.append(freq_difference)  # append the difference to the list

# Step 5: Check for Negative Frequencies
negative_count = sum(1 for freq in character_frequencies if freq < 0)  # count how many frequencies are negative

# Step 6: Output Result
if negative_count == 0:  # no negative frequencies means all characters of s2 are in s1
    print("YES")
else:
    print("NO")
