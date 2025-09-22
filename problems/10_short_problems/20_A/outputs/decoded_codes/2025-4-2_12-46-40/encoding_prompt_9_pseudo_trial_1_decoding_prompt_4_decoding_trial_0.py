import os

def normalize_path(path):
    # Remove leading and trailing whitespace
    path = path.strip()
    
    # Normalize the path using os.path.normpath to handle ".." and "."
    normalized_path = os.path.normpath(path)
    
    # Ensure there is only a single leading slash if there are multiple slashes
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    return normalized_path

def main():
    # Step 2: Receive Input
    user_input = input()
    
    # Step 3: Normalize the path
    result = normalize_path(user_input)
    
    # Step 5: Output Result
    print(result)

# Start the program
if __name__ == "__main__":
    main()
