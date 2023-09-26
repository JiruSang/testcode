import logger


if __name__ == '__main__':
    try:
        word_grid = input("please enter ne 16-character: ")
        if len(word_grid) != 16:
            print("Wrong number of characters")
        elif not word_grid.isalpha():
            print("Character should only be alphabet")
        else:
            print(word_grid)
    except Exception as e:
        logger.error(e)