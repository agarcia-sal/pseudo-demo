# Step 1: Receive Input
s1 = input()  # Input the first string
s2 = input()  # Input the second string

# Step 2: Initialize Variables
cleaned_s1 = s1.replace(" ", "")  # Remove spaces from first string
cleaned_s2 = s2.replace(" ", "")  # Remove spaces from second string

# Step 3: Initialize Frequency List
freqs = []  # List to store frequency differences

# Step 4: Calculate Character Frequencies
for x in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    # Calculate frequency difference for each character
    freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
    freqs.append(freq_difference)  # Append the frequency difference to the list

# Step 5: Check for Negative Frequencies
negative_count = sum(1 for freq in freqs if freq < 0)  # Count negative frequencies

# Step 6: Output Result
if negative_count == 0:
    print("YES")  # All frequencies are non-negative
else:
    print("NO")   # There are negative frequencies
