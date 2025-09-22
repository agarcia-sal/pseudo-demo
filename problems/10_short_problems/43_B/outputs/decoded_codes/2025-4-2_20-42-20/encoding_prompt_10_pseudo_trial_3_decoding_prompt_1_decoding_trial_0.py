# 1. Begin Program

# 2. Initialize a list s1
s1 = []
# 3. Initialize a list s2
s2 = []

# 4. Read first input and store it in variable 'first_input'
first_input = input()
# 5. Read second input and store it in variable 'second_input'
second_input = input()

# 6. For each character in 'first_input':
for char in first_input:
    # 6a. If the character is not a space:
    if char != ' ':
        # 6ai. Add the character to list s1
        s1.append(char)

# 7. For each character in 'second_input':
for char in second_input:
    # 7a. If the character is not a space:
    if char != ' ':
        # 7ai. Add the character to list s2
        s2.append(char)

# 8. Initialize a list freqs to store frequency differences
freqs = []
# 9. For each integer x from the ASCII value of 'A' to the ASCII value of 'z':
for x in range(ord('A'), ord('z') + 1):
    # 9a. Count the occurrences of the character corresponding to x in s1
    count_s1 = s1.count(chr(x))
    # 9b. Count the occurrences of the character corresponding to x in s2
    count_s2 = s2.count(chr(x))
    # 9c. Subtract the count from s2 from the count from s1
    result = count_s1 - count_s2
    # 9d. Store the result in freqs
    freqs.append(result)

# 10. Count the number of elements in freqs that are less than 0
count_negative = sum(1 for f in freqs if f < 0)
# 11. If the count is equal to 0:
if count_negative == 0:
    # 11a. Output "YES"
    print("YES")
# 12. Else:
else:
    # 12a. Output "NO"
    print("NO")

# 13. End Program
