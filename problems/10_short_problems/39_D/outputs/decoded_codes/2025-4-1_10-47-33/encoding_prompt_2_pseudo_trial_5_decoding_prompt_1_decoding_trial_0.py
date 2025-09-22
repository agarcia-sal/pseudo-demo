# 1. Start the program.

# 2. Prompt the user for input.
userInput1 = input()
userInput2 = input()

# 3. Split the input strings into individual components.
valueList1 = userInput1.split()
valueList2 = userInput2.split()

# 4. Initialize a counter for differences.
differenceCounter = 0

# 5. Compare the corresponding values from both lists.
for index in range(3):  # for each index from 0 to 2 (inclusive)
    valueA = int(valueList1[index])  # convert to integer
    valueB = int(valueList2[index])  # convert to integer
    if valueA != valueB:  # if values are not equal
        differenceCounter += 1  # increment the counter

# 6. Evaluate the total differences.
if differenceCounter < 3:
    print("YES")  # output "YES"
else:
    print("NO")  # output "NO"

# 7. End the program.
