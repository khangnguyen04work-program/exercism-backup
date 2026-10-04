def is_valid(isbn):
    nodash_isbn = isbn.replace("-", "")
    if len(nodash_isbn) != 10:
        return False

    total = 0
    multiplier = 10

    for char in nodash_isbn:
        if char.isdigit():
            value = int(char)
        elif char == "X" and multiplier == 1:
            value = 10
        else:
            return False

        total += value * multiplier
        multiplier -= 1

    return total % 11 == 0