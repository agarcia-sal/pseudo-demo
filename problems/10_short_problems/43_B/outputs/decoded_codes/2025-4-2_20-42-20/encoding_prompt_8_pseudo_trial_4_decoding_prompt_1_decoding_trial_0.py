# 1. Initialize Variables
firstInput = list()  # to store first input
secondInput = list()  # to store second input

# 2. Get Input from User
firstInput = list(input().replace(" ", ""))  # Read first string and remove spaces
secondInput = list(input().replace(" ", ""))  # Read second string and remove spaces

# 3. Count Characters Frequency
characterFrequencyDifference = []  # to hold the difference in character counts

# Loop through ASCII values for characters 'A' to 'z'
for char in range(65, 123):  
    countFirstInput = firstInput.count(chr(char))  # count in firstInput
    countSecondInput = secondInput.count(chr(char))  # count in secondInput
    difference = countFirstInput - countSecondInput  # calculate the difference
    characterFrequencyDifference.append(difference)  # add to the list

# 4. Evaluate Results
negative_count = sum(1 for x in characterFrequencyDifference if x < 0)  # count negative values

# Output decision based on negative counts
if negative_count == 0:  # if no negatives, output "YES"
    print("YES")
else:
    print("NO")  # else, output "NO"
