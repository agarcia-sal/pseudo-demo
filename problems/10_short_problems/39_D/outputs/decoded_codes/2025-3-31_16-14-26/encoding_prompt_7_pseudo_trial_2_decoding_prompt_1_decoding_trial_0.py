def main():
    # Read input from the user
    firstTimeInput = input()  # Get user input for the first time
    secondTimeInput = input()  # Get user input for the second time
    
    # Split the input strings into lists of strings
    firstTimeParts = firstTimeInput.split()  # Split first time input into parts
    secondTimeParts = secondTimeInput.split()  # Split second time input into parts
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare the parts of both time inputs
    for index in range(3):  # Loop from 0 to 2
        firstPart = int(firstTimeParts[index])  # Convert first part to integer
        secondPart = int(secondTimeParts[index])  # Convert second part to integer
        
        # Increment the difference count if parts do not match
        if firstPart != secondPart:  # Check if parts are not equal
            differenceCount += 1  # Increment the difference count
        
    # Check if there are less than 3 differences
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Main execution starts here
if __name__ == "__main__":
    main()  # Call main function
