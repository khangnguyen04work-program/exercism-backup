"""Implementation of the rotational (Caesar) cipher."""
def rotate(text, key):
    """Rotate characters in text by key positions in the alphabet."""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let_store = []
    
    for letter in text:
        if not letter.isalpha():
            let_store.append(letter)
            continue  
            
        is_cap = letter.isupper()
        clean_letter = letter.lower()

        rot = 0

        for alp_let in alphabet:
            if alp_let != clean_letter:
                rot += 1
            else: 
                rot_cipher = (rot + key) % 26 
                rot_letter = alphabet[rot_cipher]
                if is_cap:
                    rot_letter = rot_letter.upper()
                let_store.append(rot_letter)
                break
            
    concat = "".join(let_store)
    return concat
        
