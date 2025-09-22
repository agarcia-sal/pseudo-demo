# Read two lines of input, remove all space characters from each
s1 = input().replace(" ", "")
s2 = input().replace(" ", "")

freqs = []

# Iterate over character codes from 'A' (65) to 'z' (122) inclusive
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    count_s1 = s1.count(char)  # Count occurrences of char in s1
    count_s2 = s2.count(char)  # Count occurrences of char in s2
    freqs.append(count_s1 - count_s2)

# Extract all negative values from freqs
negative_freqs = [freq for freq in freqs if freq < 0]

# Output "YES" if no negative values found; otherwise, output "NO"
if len(negative_freqs) == 0:
    print("YES")
else:
    print("NO")
