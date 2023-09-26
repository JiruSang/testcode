

def clean_string(word):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in word:
        if ele in punc:
            word = word.replace(ele, "")
    return word.upper()

def convert_to_structured(word):
    array_2d = [[' ' for _ in range(4)] for _ in range(4)]

    # Populate the 2D array row by row
    index = 0
    for i in range(4):
        for j in range(4):
            array_2d[i][j] = word[index]
            index += 1
    return array_2d

def read_file_in(file_path):
    words = []

    with open(file_path, "r") as file:
        for line in file:
            words.append(line.strip())
            
    return words