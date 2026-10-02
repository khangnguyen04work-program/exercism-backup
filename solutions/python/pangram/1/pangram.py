def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',                     'w', 'x', 'y', 'z']
    formatted_sen = sentence.lower()
    count = 0
    for each_letter in alphabet:
        if each_letter in formatted_sen:
            count += 1
        elif each_letter not in formatted_sen:
            return False

    if count == 26:
        return True
    return False



