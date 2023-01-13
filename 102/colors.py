VALID_COLORS = ['blue', 'yellow', 'red']

NOT_VALID_STRING = 'Not a valid color'

def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:

        input_color = input().lower()

        if input_color == 'quit':
            print("bye")
            break
        
        elif input_color in VALID_COLORS:
            print(input_color)

        else:
            print(NOT_VALID_STRING)