"""
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

a^n + b^n = c^n

for any values of n greater than 2.

Write a function named `check_fermat` that takes four parameters—`a`, `b`, `c` and `n`—and checks to see if Fermat’s theorem holds.
If n is greater than 2 and

a^n + b^n = c^n

the program should print, “Holy smokes, Fermat was wrong!” Otherwise, the program should print,
“No, that doesn’t work.”

Write a function that prompts the user to input values for `a`, `b`, `c` and `n`,
converts them to integers, and uses `check_fermat` to check whether they violate Fermat’s theorem.
"""


def check_fermat(a, b, c, n):
    if n <= 2:
        print('Sorry, but n must be greater than 2')
    else:
        if a ** n + b ** n == c ** n:
            print('Holy smokes, Fermat was wrong!')
        else:
            print('No, that doesn’t work.')


check_fermat(1, 3, 5, 9)
