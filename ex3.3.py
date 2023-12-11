"""
Exercise 3-3.
Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated
sequence of values:

print('+', '-')

By default, print advances to the next line, but you can override that behavior
and put a space at the end, like this:

print('+', end=' ')
print('-')

The output of these statements is '+ -'.
A print statement with no argument ends the current line and goes to the next
line.
2. Write a function that draws a similar grid with four rows and four columns.
"""

# 1

def do_twice(f):
    f()
    f()


def do_4xs(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+', end='')
    print(' -' * 4, end=' ')


def print_full_beam():
    do_twice(print_beam)
    print('+')


def print_struct():
    print('|', end='')
    print(' ' * 9, end='')


def print_full_struct():
    do_twice(print_struct)
    print('|')


def print_top_half():
    print_full_beam()
    do_4xs(print_full_struct)


do_twice(print_top_half)
print_full_beam()

# 2

def print_4_beam():
    do_4xs(print_beam)
    print('+')


def print_4_struct():
    do_4xs(print_struct)
    print('|')


def print_4_half():
    print_4_beam()
    do_4xs(print_4_struct)

do_4xs(print_4_half)
print_4_beam()