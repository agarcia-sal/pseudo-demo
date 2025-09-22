import os  # Module for handling path operations
import sys  # Module for system operations
import re  # Module for regular expressions

def main():
    # Read input from user and trim any leading or trailing whitespace
    user_input = input().strip()
    
    # Normalize the path to ensure it uses the correct format for the system
    normalized_path = os.path.normpath(user_input)
    
    # Adjust leading slashes using a regular expression
    adjusted_path = re.sub(r'^/+', '/', normalized_path)
    
    # Output the final adjusted path
    print(adjusted_path)

if __name__ == "__main__":
    main()
