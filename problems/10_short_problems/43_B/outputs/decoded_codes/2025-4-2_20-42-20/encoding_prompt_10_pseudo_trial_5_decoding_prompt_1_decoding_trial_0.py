# 1. Receive Input:
s1 = input()
s2 = input()

# 2. Initialize Variables:
cleaned_s1 = s1.replace(" ", "")
cleaned_s2 = s2.replace(" ", "")

# 3. Initialize Frequency List:
freqs = []

# 4. Calculate Character Frequencies:
for x in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    freq_difference = cleaned_s1.count(chr(x)) - cleaned_s2.count(chr(x))
    freqs.append(freq_difference)

# 5. Check for Negative Frequencies:
negative_count = sum(1 for freq in freqs if freq < 0)

# 6. Output Result:
if negative_count == 0:
    print("YES")
else:
    print("NO")
