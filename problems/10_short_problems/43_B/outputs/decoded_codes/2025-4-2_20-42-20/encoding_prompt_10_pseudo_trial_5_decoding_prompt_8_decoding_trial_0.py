# Receive Input
s1 = input()
s2 = input()

# Initialize Variables
cleaned_s1 = s1.replace(" ", "")
cleaned_s2 = s2.replace(" ", "")

# Initialize Frequency List
freqs = []

# Calculate Character Frequencies
for x in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
    freqs.append(freq_difference)

# Check for Negative Frequencies
negative_count = sum(1 for freq in freqs if freq < 0)

# Output Result
if negative_count == 0:
    print("YES")
else:
    print("NO")


def compare_strings(s1, s2):
    cleaned_s1 = s1.replace(" ", "")
    cleaned_s2 = s2.replace(" ", "")

    freqs = []
    for x in range(65, 123):
        freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
        freqs.append(freq_difference)

    negative_count = sum(1 for freq in freqs if freq < 0)

    return "YES" if negative_count == 0 else "NO"

# Example usage
s1 = input()
s2 = input()
result = compare_strings(s1, s2)
print(result)
