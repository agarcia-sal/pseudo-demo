def main():
    # Read two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into individual values and store them in lists
    firstValues = firstLine.split()
    secondValues = secondLine.split()
    
    # Initialize a counter to count the number of differing values
    differenceCount = 0
    
    # Loop through the first three values of both lists
    for index in range(3):
        # Convert the current values from strings to integers
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])
        
        # If the current values do not match, increase the difference counter
        if valueFromFirst != valueFromSecond:
            differenceCount += 1
            
    # After checking all values, determine if the differences are acceptable
    if differenceCount < 3:
        print("YES")  # The values differ in fewer than three positions
    else:
        print("NO")   # The values differ in three or more positions
        
# Call the main function to execute the program
main()
