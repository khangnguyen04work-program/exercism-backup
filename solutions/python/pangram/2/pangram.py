"""Determine if a sentence is a pangram."""


def is_pangram(sentence):
    """Check whether every letter of the alphabet is in the given sentence."""
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    formatted_sen = sentence.lower()

    for each_letter in alphabet:
        if each_letter not in formatted_sen:
            return False

    return True