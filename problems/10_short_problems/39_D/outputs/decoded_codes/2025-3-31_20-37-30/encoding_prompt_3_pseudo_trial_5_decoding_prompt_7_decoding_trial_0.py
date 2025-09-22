def main():
    # Read input from the user
    firstString = input()
    secondString = input()
    
    # Split the input strings into lists of strings
    firstList = firstString.split()
    secondList = secondString.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Loop through each corresponding element in both lists
    for index in range(3):  # Looping over fixed range as we have exactly 3 elements
        # Convert the elements to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the two values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1
    
    # If the number of differences is less than 3, print "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Entry point of the program
main()
