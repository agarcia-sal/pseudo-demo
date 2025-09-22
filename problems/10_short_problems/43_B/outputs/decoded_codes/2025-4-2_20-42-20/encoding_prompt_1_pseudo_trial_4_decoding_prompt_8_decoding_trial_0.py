# Step 1: Input Two Strings
s1 = input().replace(" ", "")
s2 = input().replace(" ", "")

# Step 2: Create Character Frequency Difference
# Initialize a list for frequency differences
frequency_difference = []

# Check character frequency for ASCII range from 'A' to 'z'
for char_code in range(65, 123):  # 65 is 'A' and 122 is 'z'
    count_s1 = s1.count(chr(char_code))  # Count in first string
    count_s2 = s2.count(chr(char_code))  # Count in second string
    difference = count_s1 - count_s2      # Calculate difference
    frequency_difference.append(difference)  # Store the difference

# Step 3: Check for Negative Differences
negative_count = sum(1 for diff in frequency_difference if diff < 0)  # Count negatives

# Output results
if negative_count == 0:
    print("YES")
else:
    print("NO")


     abc
     abc
     

     aabbcc
     abc
     

     abc
     aabbcc
     

     
     abc
     

     a b c
     bc
     