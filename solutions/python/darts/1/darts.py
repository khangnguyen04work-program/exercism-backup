def score(x, y):
    simpleEqua = (x**2 + y**2)
    if simpleEqua > 10**2:
        return 0
    if simpleEqua <= 1**2:
        return 10
    elif simpleEqua <= 5**2:
        return 5
    elif simpleEqua <= 10**2:
        return 1
        
    
    