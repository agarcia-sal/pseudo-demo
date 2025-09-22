# Function to compare two sets of three numbers
def compare_number_sets():
    # Step 2: Receive Input
    firstSet = []  # List for the first set of numbers
    secondSet = []  # List for the second set of numbers
    
    # Read numbers for the first set
    for i in range(3):
        firstSet.append(int(input()))  # Convert input to integer and add to firstSet
    
    # Read numbers for the second set
    for i in range(3):
        secondSet.append(int(input()))  # Convert input to integer and add to secondSet
    
    # Step 3: Initialize Difference Count
    differenceCount = 0  # Variable to keep track of differences
    
    # Step 4: Loop through the Sets
    for index in range(3):  # Loop over indices 0, 1, 2
        if firstSet[index] != secondSet[index]:  # Check if numbers at the current index are different
            differenceCount += 1  # Increment count if they are not equal
    
    # Step 5: Check the Number of Differences
    if differenceCount < 3:  # If there are fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise output "NO"

# Step 7: Execution of Program
compare_number_sets()  # Invoke the function to run the program
