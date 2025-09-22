import os

def main():
    # Step 1: Read a file path input from standard input
    input_path = input()
    
    # Step 2: Normalize the file path by removing redundant separators
    normalized_path = os.path.normpath(input_path)
    
    # Step 3: Replace any leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        cleaned_path = '/' + normalized_path.lstrip('/')
    else:
        cleaned_path = normalized_path
    
    # Step 4: Output the cleaned path
    print(cleaned_path)

if __name__ == "__main__":
    main()
