def main():
    # Read two lines of input
    terminalInput1 = input()
    terminalInput2 = input()
    
    # Split the input strings into lists of strings
    list1 = terminalInput1.split()
    list2 = terminalInput2.split()

    # Initialize a counter for differences
    differenceCounter = 0

    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the current elements to integers
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Check if the two numbers are different
        if number1 != number2:
            # Increment the difference counter
            differenceCounter += 1
            
    # Check how many differences were found
    if differenceCounter < 3:
        # Output "YES" if less than 3 differences
        print("YES")
    else:
        # Output "NO" if 3 or more differences
        print("NO")
    
# Execute the main function
main()
