def processEmailAddress(inputString):
    # Read input from standard input and remove leading or trailing whitespace
    emailAddress = inputString.strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    emailAddress = emailAddress.replace('dot', '.')
    emailAddress = emailAddress.replace('at', '@')

    # Check if the email starts with '.', prepend 'dot' if necessary
    if emailAddress.startswith('.'):
        emailAddress = 'dot' + emailAddress[1:]

    # Initialize a counter and a list to rebuild the email
    counter = 0
    emailParts = []
    
    # Check if the email starts with '@', prepend 'at' if necessary
    if emailAddress.startswith('@'):
        emailAddress = 'at' + emailAddress[1:]

    # Iterate through each character in the email string
    for character in emailAddress:
        if character == '@':
            # If '@' is found and counter is greater than 0, add 'at' to the list
            if counter > 0:
                emailParts.append('at')
                counter = 1 
            else:
                emailParts.append('@')
                counter = 1
        else:
            # Append the current character to the list
            emailParts.append(character)

    # Join the list into a string
    reconstructedEmail = ''.join(emailParts)

    # If the reconstructed email ends with '.', replace it with 'dot'
    if reconstructedEmail.endswith('.'):
        reconstructedEmail = reconstructedEmail[:-1] + 'dot'

    # Output the processed email address
    print(reconstructedEmail)

# Example test cases
if __name__ == "__main__":
    # Test case 1: normal case
    processEmailAddress("userdotdomainatgmaildotcom")
    # Test case 2: starts with a dot
    processEmailAddress(".userdotdomainatgmaildotcom")
    # Test case 3: starts with at
    processEmailAddress("@userdotdomaindotcom")
    # Test case 4: ends with a dot
    processEmailAddress("userdotdomainatgmaildotcom.")
    # Test case 5: multiple at and dot replacements
    processEmailAddress("firstdotlastatcompanydotcom")
