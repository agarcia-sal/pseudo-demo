def main():
    # Read input from the user
    firstTimeInput = input()
    secondTimeInput = input()
    
    # Split the input strings into lists of strings
    firstTimeParts = firstTimeInput.split()
    secondTimeParts = secondTimeInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare the parts of both time inputs
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        firstPart = int(firstTimeParts[index])  # Convert to integer
        secondPart = int(secondTimeParts[index])  # Convert to integer
        
        # Increment the difference count if parts do not match
        if firstPart != secondPart:
            differenceCount += 1 
    
    # Check if there are less than 3 differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
