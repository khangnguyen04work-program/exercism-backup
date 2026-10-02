"""Module providing a function yo define whether the word/phrase is isogram or not."""



def is_isogram(phrase):
    """Compare each letter in word/phrase to its following one after being formatted"""
    formatted = phrase.lower()
    formatted_again = formatted.replace(" ", "")
    char_num = len(formatted_again)
    index = 0
    for each_char in formatted_again:
        index += 1
        if each_char in formatted_again[index:(char_num + 1)] and each_char != "-":
            return False
    return True
    