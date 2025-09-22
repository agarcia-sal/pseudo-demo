import os

def normalize_path(input_path):
    # Normalize the path using os.path.normpath to handle '.' and '..'
    return os.path.normpath(input_path)

def adjust_leading_slashes(normalized_path):
    # Remove all leading slashes and keep only one if there were any
    if normalized_path.startswith('/'):
        return '/' + normalized_path.lstrip('/')
    return normalized_path.lstrip('/')

def main():
    # Step 1: Read the input from the user
    input_path = input().strip()  # read input and strip extra spaces
    
    # Step 2: Normalize the file path
    normalized_path = normalize_path(input_path)
    
    # Step 3: Adjust the path
    output_path = adjust_leading_slashes(normalized_path)
    
    # Step 4: Print the result
    print(output_path)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
