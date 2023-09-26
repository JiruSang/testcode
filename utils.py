

def cleanString(word):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in word:
        if ele in punc:
            word = word.replace(ele, "")
    return word.upper()

