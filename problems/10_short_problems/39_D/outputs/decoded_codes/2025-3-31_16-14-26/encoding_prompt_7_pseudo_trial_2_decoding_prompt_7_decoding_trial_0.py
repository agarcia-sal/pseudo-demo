def main():
    # Read input from the user
    firstTimeInput = input()  # Get user input for the first time
    secondTimeInput = input()  # Get user input for the second time
    
    # Split the input strings into lists of strings
    firstTimeParts = firstTimeInput.split(':')  # Split first time into parts
    secondTimeParts = secondTimeInput.split(':')  # Split second time into parts
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare the parts of both time inputs
    for index in range(3):  # Iterate over the three parts (hours, minutes, seconds)
        firstPart = int(firstTimeParts[index])  # Convert first part to integer
        secondPart = int(secondTimeParts[index])  # Convert second part to integer
        
        # Increment the difference count if parts do not match
        if firstPart != secondPart:  # Check if the parts are not equal
            differenceCount += 1  # Increment the difference count
    
    # Check if there are less than 3 differences
    if differenceCount < 3:  # If fewer than 3 parts differ
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Main execution starts here
if __name__ == "__main__":  # If the script is run as the main program
    main()  # Call the main function
