# Function to clean a word by removing punctuation and converting it to uppercase
def clean_string(word):
    # Define a string containing punctuation characters to remove
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Iterate through each character in the word
    for ele in word:
        # Check if the character is in the punctuation string
        if ele in punc:
            # If it's a punctuation character, replace it with an empty string
            word = word.replace(ele, "")

    # Convert the cleaned word to uppercase and return it
    return word.upper()


# Function to convert a string into a 2D array of specified dimensions (4x4)
def convert_to_structured(word):
    # Initialize an empty 4x4 2D array
    array_2d = [[' ' for _ in range(4)] for _ in range(4)]

    # Populate the 2D array row by row
    index = 0
    for i in range(4):
        for j in range(4):
            # Assign characters from the input word to the 2D array
            array_2d[i][j] = word[index]
            index += 1

    # Return the populated 2D array
    return array_2d


# Function to read words from a file and store them in a list
def read_file_in(file_path):
    # Initialize an empty list to store the words
    words = []

    # Open the specified file in read mode
    with open(file_path, "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading and trailing whitespace from each line and add it to the list
            words.append(line.strip())

    # Return the list of words
    return words
