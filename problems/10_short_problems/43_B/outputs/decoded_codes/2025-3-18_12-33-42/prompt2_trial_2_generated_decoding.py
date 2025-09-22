# Step 1: Read two lines of input and remove spaces
first_input = input().replace(" ", "")
second_input = input().replace(" ", "")

# Step 2: Initialize the frequencyDifference list
frequencyDifference = []

# Step 3: Calculate the difference in character counts
for char in range(ord('A'), ord('z') + 1):
    count_first = first_input.count(chr(char))
    count_second = second_input.count(chr(char))
    frequencyDifference.append(count_first - count_second)

# Step 4: Assess the frequencyDifference list
if any(count < 0 for count in frequencyDifference):
    # If there's any count < 0, output "NO"
    print("NO")
else:
    # Otherwise, output "YES"
    print("YES")
