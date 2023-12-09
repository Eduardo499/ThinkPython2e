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