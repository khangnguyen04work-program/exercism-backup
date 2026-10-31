"""Calculate the points scored in a single toss of a Darts game!"""

def score(x, y):
    """Check to see if the coordinate is in/out of circle and which point level it belongs to using (x-h)^2 + (y-k)^2 = r^2 formula"""
    main_equation = x**2 + y**2
    if main_equation > 10**2:
        return 0
    if main_equation <= 1**2:
        return 10
    elif main_equation <= 5**2:
        return 5
    elif main_equation <= 10**2:
        return 1
        
    
    