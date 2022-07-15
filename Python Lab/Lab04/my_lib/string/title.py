def title(string: str):
    words = string.lower().split()
    new_string = ""
    for word in words:
        first_char: str = word[0]
        first_char_uppercase = first_char.upper()
        new_string += first_char_uppercase + word[1:] + " "
    return new_string.strip()
