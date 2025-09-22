# 1. Start the Program

# 2. Receive Input:
first_set_input = input()  # Get the first set of numbers from the user
second_set_input = input()  # Get the second set of numbers from the user

# 3. Split Input into Individual Numbers:
firstSet = first_set_input.split()  # Break the first set of numbers into a list
secondSet = second_set_input.split()  # Break the second set of numbers into a list

# 4. Initialize a Difference Counter:
differenceCount = 0  # Set a variable to 0 to count differences

# 5. Compare Corresponding Numbers:
for index in range(3):  # For each index from 0 to 2 (inclusive)
    firstNumber = int(firstSet[index])  # Convert to integer
    secondNumber = int(secondSet[index])  # Convert to integer
    if firstNumber != secondNumber:  # If not equal
        differenceCount += 1  # Increment the difference count by 1

# 6. Check the Number of Differences:
if differenceCount < 3:  # If fewer than 3 differences
    print("YES")  # Output "YES"
else:  # Otherwise
    print("NO")  # Output "NO"

# 7. End of Program
