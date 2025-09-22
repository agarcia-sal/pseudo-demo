# BEGIN

# Read input line and remove any extra whitespace
emailInput = input().strip()  # equivalent to TRIM(emailInput)

# Replace specific words with designated symbols
emailInput = emailInput.replace('dot', '.')  # equivalent to REPLACE 'dot' WITH '.' IN emailInput
emailInput = emailInput.replace('at', '@')    # equivalent to REPLACE 'at' WITH '@' IN emailInput

# Ensure the email starts with 'dot' if it starts with a period
if emailInput.startswith('.'):
    emailInput = 'dot' + emailInput[1:]  # equivalent to 'dot' + REST of emailInput starting from index 1

# Initialize variables for processing
countOfAtSymbols = 0
modifiedEmail = []  # using a list to accumulate characters
index = 0  # although not used, included for structural flow

# Ensure the email starts with 'at' if it starts with '@'
if emailInput.startswith('@'):
    emailInput = 'at' + emailInput[1:]  # equivalent to 'at' + REST of emailInput starting from index 1

# Loop through each character in the emailInput
for character in emailInput:
    if character == '@':
        # If we have already encountered an '@', add 'at'
        if countOfAtSymbols > 0:
            modifiedEmail.append('at')  # equivalent to ADD 'at' TO modifiedEmail
            countOfAtSymbols = 1  # maintaining count of symbols
        else:
            modifiedEmail.append('@')  # equivalent to ADD '@' TO modifiedEmail
            countOfAtSymbols = 1
    else:
        # For any other character, simply add it to the list
        modifiedEmail.append(character)  # equivalent to ADD character TO modifiedEmail

# Join the modified characters into a single string
modifiedEmail = ''.join(modifiedEmail)  # equivalent to JOIN characters in modifiedEmail into a single string

# Ensure the email does not end with a period
if modifiedEmail.endswith('.'):
    modifiedEmail = modifiedEmail[:-1] + 'dot'  # equivalent to REMOVE last character and ADD 'dot' to modifiedEmail

# Output the final formatted email
print(modifiedEmail)  # equivalent to PRINT modifiedEmail

# END
