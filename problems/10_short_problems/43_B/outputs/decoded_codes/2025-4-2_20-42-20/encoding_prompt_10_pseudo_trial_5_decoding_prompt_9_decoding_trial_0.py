# Request user input for two strings
s1 = input()
s2 = input()

# Remove spaces from the input strings
cleaned_s1 = s1.replace(" ", "")
cleaned_s2 = s2.replace(" ", "")

# Initialize a list to hold frequency differences
freqs = []

# Calculate character frequencies from ASCII 'A' (65) to 'z' (122)
for x in range(65, 123):
    # Count occurrences of the character in both cleaned strings
    freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
    # Append the difference to the list
    freqs.append(freq_difference)

# Count the number of negative frequencies in the list
negative_count = sum(1 for freq in freqs if freq < 0)

# Output the result based on the negative frequencies
if negative_count == 0:
    print("YES")
else:
    print("NO")
