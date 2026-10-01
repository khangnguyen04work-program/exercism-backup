def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    fomattedText = text.split()
    word_container = []
    
    for fText in fomattedText:
        # Rule 1
        if fText[0] in vowels or fText[0:2] == "xr" or fText[0:2] == "yt":
            new_txt = fText + "ay"
            word_container.append(new_txt)
            continue
        
        # Rule 3
        if fText[0] in consonants and fText[1:3] == "qu":
            moved_cons_3_two = fText[3:] + fText[0:3]
            new_txt3_two = moved_cons_3_two + "ay"  
            word_container.append(new_txt3_two)
            continue
            
        elif fText[0:2] == "qu":
            moved_cons_3_one = fText[2:] + fText[0:2]
            new_txt3_one = moved_cons_3_one + "ay"
            word_container.append(new_txt3_one)
            continue
       
        # Rule 2
        specific_con = []
        rule2_applied = False  # Flag to determine if we should skip Rule 4
        
        for compoundCon in fText[0:]:
            if compoundCon in consonants:
                specific_con.append(compoundCon)
            elif compoundCon in vowels:
                countCon = len(specific_con)
                moved_cons_2 = fText[countCon:] + fText[0:countCon]
                new_txt2 =  moved_cons_2 + "ay"
                word_container.append(new_txt2)
                rule2_applied = True
                break  # Exits the inner character loop
                
        # If Rule 2 successfully found a vowel and appended the word, move to the next word
        if rule2_applied:
            continue
        
        # Rule 4 (Will now only execute for words with no vowels, like "my" or "rhythm")
        specific_con4 = []
        for compoundCon_4 in fText[0:]:
            if compoundCon_4 in consonants and compoundCon_4 != "y":
                specific_con4.append(compoundCon_4)
            elif compoundCon_4 == "y":
                countCon_4  = len(specific_con4)
                movedCon_4 = fText[countCon_4:] + fText[0:countCon_4]
                new_txt4 = movedCon_4 + "ay"
                word_container.append(new_txt4)
                break
                
    return " ".join(word_container)