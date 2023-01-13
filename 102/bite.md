In this Bite we'll get you to take user input using the `input` builtin and see if it matches items within a list.


In the `while` loop ask the user to enter a color and capture that input.


Check to see whether they've entered 'quit'. If so, print *bye* and exit (`break`) the loop, effectively ending the function.


If not, check to see whether the color (input) is in the `VALID_COLORS` color list. If it is, then print the color **in lower case**. If not, print *Not a valid color* and `continue` the loop. Then conclude by printing *bye*.


*For this exercise the tests check standard output (what you print) so it's important to not print anything else (e.g. a string asking the user to enter a color), nor invoke the `print_colors()` function at the bottom of your code. It will fail the tests.*


As you want to ask the user over and over again till they quit, you can use an infinite `while` loop. We already provided that in the template code, just code inside that loop.

