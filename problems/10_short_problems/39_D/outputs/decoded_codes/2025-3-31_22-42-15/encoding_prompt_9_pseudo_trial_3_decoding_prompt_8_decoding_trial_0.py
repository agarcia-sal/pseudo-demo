def main():
    # Get two input strings representing numerical values
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of numerical strings
    numbersFromFirstSet = firstSet.split()
    numbersFromSecondSet = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the range of three positions
    for position in range(3):
        # Convert the current positions' values from strings to integers
        valueFromFirstSet = int(numbersFromFirstSet[position])
        valueFromSecondSet = int(numbersFromSecondSet[position])

        # Check if the values from both sets differ
        if valueFromFirstSet != valueFromSecondSet:
            # Increment the difference counter
            differenceCount += 1

    # Check the total differences and decide the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()


   Expected Output: `YES`

2. **One Difference**: 
   

   Expected Output: `YES`

3. **Two Differences**: 
   

   Expected Output: `YES`

4. **Three Differences**: 
   

   Expected Output: `NO`

5. **Mixed Values** (testing negative and zero):
   

   Expected Output: `YES`

6. **Edge Case: Negative Numbers**: 
   