def main():
    # Read input values for the two times
    firstTime = input()
    secondTime = input()
    
    # Split the input strings into lists of components
    components1 = firstTime.split()
    components2 = secondTime.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare corresponding components of both times
    for index in range(3):  # We expect exactly 3 components (hour, minute, second)
        # Convert components to integers
        value1 = int(components1[index])
        value2 = int(components2[index])
        
        # Check if the values are different
        if value1 != value2:
            differenceCount += 1  # Increment the counter if values are different
    
    # Determine result based on the number of differences
    if differenceCount < 3:
        print("YES")  # If differences are less than 3, print YES
    else:
        print("NO")   # If differences are 3 or more, print NO

# Start the main function when the script runs
if __name__ == "__main__":
    main()
