'''
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
'''
name = "svyatoslav"
day = "saturday"
print('The first way to format a string: \n', f"Good day {name.title()}! {day.title()} is a perfect day to learn some python.")
print('The second way to format a string: \n', 'Good day {1}! {0} is a perfect day to learn some python.'.format(day.title(), name.title()))
print('The third way to format a string: \n', 'Good day %s! %s is a perfect day to learn some python.' % (name.title(), day.title()))