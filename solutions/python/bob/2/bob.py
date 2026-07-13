"""Module for determining how Bob the teenager responds to input."""


def response(hey_bob):
    text = hey_bob.strip()
    if text.isupper() and text.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if text.isupper():
        return "Whoa, chill out!"
    if text.endswith("?"):
        return "Sure."
    if not text:
        return "Fine. Be that way!"

    return "Whatever."