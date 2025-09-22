# Step 1: Input Two Strings
# Read the first string from user input, removing spaces
s1 = input().replace(" ", "")
# Read the second string from user input, removing spaces
s2 = input().replace(" ", "")

# Step 2: Create Character Frequency Difference
# Initialize a list to hold the frequency differences of all characters from 'A' to 'z'
# The range of ASCII characters we care about is from 65 ('A') to 122 ('z')
char_diff = [0] * (123)  # 123 is used to include index 122

# Loop through the ASCII range of characters
for char_code in range(65, 123):
    # Count occurrences of the current character in both strings
    count_s1 = s1.count(chr(char_code))  # Count in string 1
    count_s2 = s2.count(chr(char_code))  # Count in string 2
    
    # Calculate the difference and store in the list
    char_diff[char_code] = count_s1 - count_s2

# Step 3: Check for Negative Differences
# Count how many differences in the list are less than zero
negative_count = sum(1 for diff in char_diff if diff < 0)  # Using a generator expression for succinctness

# Determine if all differences are non-negative
if negative_count == 0:
    print("YES")  # All characters in s1 are sufficient for s2
else:
    print("NO")  # Some characters in s1 are insufficient for s2
