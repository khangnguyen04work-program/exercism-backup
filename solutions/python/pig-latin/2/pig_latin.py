"""Module providing a function to translate English text into Pig Latin."""

def translate(text):
    """Function translating text to Pig Latin based on specific consonant and vowel rules."""
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    formatted_text = text.split()
    word_container = []
    
    for f_text in formatted_text:
        # Rule 1
        if f_text[0] in vowels or f_text[0:2] == "xr" or f_text[0:2] == "yt":
            new_txt = f_text + "ay"
            word_container.append(new_txt)
            continue
        
        # Rule 3
        if f_text[0] in consonants and f_text[1:3] == "qu":
            moved_cons_3_two = f_text[3:] + f_text[0:3]
            new_txt3_two = moved_cons_3_two + "ay"  
            word_container.append(new_txt3_two)
            continue
            
        if f_text[0:2] == "qu":
            moved_cons_3_one = f_text[2:] + f_text[0:2]
            new_txt3_one = moved_cons_3_one + "ay"
            word_container.append(new_txt3_one)
            continue
       
        # Rule 2
        specific_con = []
        rule2_applied = False
        
        for compound_con in f_text[0:]:
            if compound_con in consonants:
                specific_con.append(compound_con)
            elif compound_con in vowels:
                count_con = len(specific_con)
                moved_cons_2 = f_text[count_con:] + f_text[0:count_con]
                new_txt2 = moved_cons_2 + "ay"
                word_container.append(new_txt2)
                rule2_applied = True
                break
                
        if rule2_applied:
            continue
        
        # Rule 4
        specific_con4 = []
        for compound_con_4 in f_text[0:]:
            if compound_con_4 in consonants and compound_con_4 != "y":
                specific_con4.append(compound_con_4)
            elif compound_con_4 == "y":
                count_con_4 = len(specific_con4)
                moved_con_4 = f_text[count_con_4:] + f_text[0:count_con_4]
                new_txt4 = moved_con_4 + "ay"
                word_container.append(new_txt4)
                break
                
    return " ".join(word_container)