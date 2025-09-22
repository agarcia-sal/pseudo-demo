def main():
    # Read two sets of input from the user
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into individual elements
    firstValues = firstSet.split()
    secondValues = secondSet.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through each pair of corresponding values
    for index in range(3):
        # Convert the string values to integers
        valueFromFirstSet = int(firstValues[index])
        valueFromSecondSet = int(secondValues[index])
        
        # Check if the values are different
        if valueFromFirstSet != valueFromSecondSet:
            differenceCount += 1
            
    # Check if the number of differences is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution begins here
main()
