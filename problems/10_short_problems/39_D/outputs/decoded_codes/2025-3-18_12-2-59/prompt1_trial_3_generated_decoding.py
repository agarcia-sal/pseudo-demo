def main():
    # Read two lines of input representing two sets of three integers
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into lists of strings
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the two values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1
    
    # If the number of differences is less than three, output "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Execute the main function if the script is run as the main program
if __name__ == "__main__":
    main()
