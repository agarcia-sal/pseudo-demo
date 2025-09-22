def main():
    # Read input values
    firstTime = input()
    secondTime = input()
    
    # Split the input strings into lists
    components1 = firstTime.split()
    components2 = secondTime.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare corresponding components of both times
    for index in range(3):
        # Convert components to integers
        value1 = int(components1[index])
        value2 = int(components2[index])
        
        # Check if the values are different
        if value1 != value2:
            differenceCount += 1
    
    # Determine result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the main function when the script runs
main()
