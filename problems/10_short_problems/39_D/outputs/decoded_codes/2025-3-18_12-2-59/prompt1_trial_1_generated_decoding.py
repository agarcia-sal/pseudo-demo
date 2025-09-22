def main():
    # Read two lines of input representing two sets of values
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into lists of values
    values1 = firstSet.split()
    values2 = secondSet.split()
    
    # Initialize a counter for the number of differing values
    differingCount = 0 
    
    # Loop through the first three elements in both lists
    for index in range(3):
        # Convert the current elements to integers
        valueFromFirstSet = int(values1[index])
        valueFromSecondSet = int(values2[index])
        
        # Check if the current elements are different
        if valueFromFirstSet != valueFromSecondSet:
            # Increment the counter for differing values
            differingCount += 1
    
    # Evaluate the count of differing values
    if differingCount < 3:
        # If less than 3 differences, output "YES"
        print("YES")
    else:
        # If 3 or more differences, output "NO"
        print("NO")

# Start the program execution
main()
