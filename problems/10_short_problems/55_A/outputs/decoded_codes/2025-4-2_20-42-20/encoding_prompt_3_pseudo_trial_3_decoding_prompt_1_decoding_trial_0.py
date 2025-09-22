# Read an integer input representing the size of the list
sizeToCheck = int(input())

# Initialize a list to track boolean values for numbers up to sizeToCheck
isChecked = [True] * sizeToCheck

# Initialize counter variables
index = 0
increment = 1

# Loop while increment is less than or equal to 500,000
while increment <= 500000:
    
    # If the current position (index) in the list is still TRUE
    if isChecked[index] == True:
        
        # Mark the current position as FALSE (checked)
        isChecked[index] = False
        
    # Increment the value of increment
    increment += 1
    
    # Update the index based on the current increment value
    index = (index + increment) % sizeToCheck

# Create a filtered list of items in isChecked that are still TRUE
remainingTrueItems = [item for item in isChecked if item]

# Check if there are any TRUE values left in the remainingTrueItems list
if len(remainingTrueItems) == 0:
    # If no TRUE items are left, print 'YES'
    print('YES')
else:
    # If there are TRUE items left, print 'NO'
    print('NO')
