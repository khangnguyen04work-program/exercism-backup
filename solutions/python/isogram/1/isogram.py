def is_isogram(phrase):
    formatted = phrase.lower()
    formatted_again = formatted.replace(" ", "")
    charNUM = len(formatted_again)
    index = 0
    for each_char in formatted_again:
        index += 1
        if each_char in formatted_again[index:(charNUM + 1)] and each_char != "-":
            return False
    return True
    