# Define the main function to compare two sets of numbers
def compare_number_sets():
    # Receive input for the first and second sets
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into lists of numbers
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize a counter for the number of differences
    differenceCount = 0
    
    # Compare the numbers at each index in the lists
    for index in range(3):  # Indices 0, 1, 2
        # Convert the strings to integers for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Determine the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison when the script runs
compare_number_sets()
